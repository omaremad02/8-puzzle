import heapq
import math
from collections import deque
import time

goal_state = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]
max_depth = 1000000


class State:
    def __init__(self, shape, parent=None, move=None, depth=0):
        self.shape = shape
        self.map = ''.join([''.join(map(str, row)) for row in shape])
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return self.depth < other.depth


def expand(state):
    children = []
    blank_row, blank_col = None, None
    for i in range(3):
        for j in range(3):
            if state.shape[i][j] == 0:
                blank_row, blank_col = i, j
                break
    possible_moves = []
    if blank_col != 2:
        possible_moves.append((0, 1))  # RIGHT
    if blank_col != 0:
        possible_moves.append((0, -1))  # LEFT
    if blank_row != 0:
        possible_moves.append((-1, 0))  # UP
    if blank_row != 2:
        possible_moves.append((1, 0))  # DOWN
    for move_tuple in possible_moves:
        new_row, new_col = blank_row + move_tuple[0], blank_col + move_tuple[1]
        if move_tuple == (-1, 0):
            move = "Up"
        elif move_tuple == (1, 0):
            move = "Down"
        elif move_tuple == (0, -1):
            move = "Left"
        elif move_tuple == (0, 1):
            move = "Right"
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            child_shape = [row[:] for row in state.shape]
            child_shape[blank_row][blank_col], child_shape[new_row][new_col] = \
                child_shape[new_row][new_col], child_shape[blank_row][blank_col]
            child_state = State(child_shape, state, move, state.depth + 1)
            children.append(child_state)
    return children


def bfs(initial_state, goal_state):
    start_time = time.time()
    explored, frontier = set(), deque([State(initial_state)])
    expanded = 0

    while frontier:
        current_state = frontier.popleft()
        explored.add(current_state.map)
        expanded += 1

        if current_state.shape == goal_state:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return current_state, expanded, elapsed_time

        neighbours = expand(current_state)
        for neighbour in neighbours:
            if neighbour.map not in explored and not any(neighbour.map == f_state.map for f_state in frontier):
                frontier.append(neighbour)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return None, expanded, elapsed_time


def dfs(initial_state, goal_state):
    start_time = time.time()
    explored, frontier = set(), list([State(initial_state)])
    expanded = 0

    while frontier:
        current_state = frontier.pop()
        explored.add(current_state.map)
        expanded += 1

        if current_state.shape == goal_state:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return current_state, expanded, elapsed_time

        if current_state.depth < max_depth:
            neighbours = expand(current_state)
            for neighbour in neighbours:
                if neighbour.map not in explored and not any(neighbour.map == f_state.map for f_state in frontier):
                    frontier.append(neighbour)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return None, expanded, elapsed_time


def manhattan_distance(current_state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != 0:
                goal_row, goal_col = get_goal_position(current_state[i][j], goal_state)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance


def euclidean_distance(current_state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != 0:
                goal_row, goal_col = get_goal_position(current_state[i][j], goal_state)
                distance += math.sqrt((i - goal_row) ** 2 + (j - goal_col) ** 2)
    return distance


def get_goal_position(value, goal_state):
    for i in range(3):
        for j in range(3):
            if goal_state[i][j] == value:
                return i, j


def a_star_search(initial_state, goal_state, heuristic):
    start_time = time.time()
    frontier = []
    explored = set()
    expanded = 0

    heapq.heappush(frontier, (0, State(initial_state)))
    while frontier:
        _, current_state = heapq.heappop(frontier)
        explored.add(current_state.map)
        expanded += 1

        if current_state.shape == goal_state:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return current_state, expanded, elapsed_time

        for neighbour in expand(current_state):
            priority = neighbour.depth + heuristic(neighbour.shape, goal_state)
            if neighbour.map not in explored and not any(neighbour.map == f_state[1].map for f_state in frontier):
                heapq.heappush(frontier, (priority, neighbour))
            else:
                existing_index = None
                for i, (priority, state) in enumerate(frontier):
                    if state.shape == neighbour.shape:
                        existing_index = i
                        break

                if existing_index is not None and frontier[existing_index][0] > priority:
                    frontier[existing_index] = (priority, neighbour)
                    heapq.heapify(frontier)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return None, expanded, elapsed_time


def isSolvable(state):
    inversion_count = 0
    flatten_puzzle = []
    for row in state:
        for tile in row:
            if tile != 0:
                flatten_puzzle.append(tile)

    for i in range(len(flatten_puzzle)):
        for j in range(i + 1, len(flatten_puzzle)):
            if flatten_puzzle[i] > flatten_puzzle[j]:
                inversion_count += 1
    return inversion_count % 2 == 0


initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

if not isSolvable(initial_state):
    print("This cannot be solved.")

else:
    state, expanded, elapsed_time = a_star_search(initial_state, goal_state, euclidean_distance)
    print("A* Search:")
    print("Expanded:", expanded)
    print("Time Elapsed:", elapsed_time, "seconds")
    if state:
        print("Depth:", state.depth)
        solution = []
        while state:
            if state.move:
                solution.append((state.move, state.shape))
            state = state.parent
        solution.reverse()
        for move, shape in solution:
            print(f'Move: {move}')
           # for row in shape:
              #  print(row)
           # print()
    else:
        print("Failed")
    print("-------------------------------------------------------")
    state, expanded, elapsed_time = dfs(initial_state, goal_state)
    print("DFS: ")
    print("Expanded:", expanded)
    print("Time Elapsed:", elapsed_time, "seconds")
    if state:
        print("Depth:", state.depth)
        solution = []
        while state:
            if state.move:
                solution.append((state.move, state.shape))
            state = state.parent
        solution.reverse()
        for move, shape in solution:
            print(f'Move: {move}')
            #for row in shape:
               # print(row)
           # print()
    else:
        print("Failed")
    print("-------------------------------------------------------")
    state, expanded, elapsed_time = bfs(initial_state, goal_state)
    print("BFS: ")
    print("Expanded:", expanded)
    print("Time Elapsed:", elapsed_time, "seconds")
    if state:
        print("Depth:", state.depth)
        solution = []
        while state:
            if state.move:
                solution.append((state.move, state.shape))
            state = state.parent
        solution.reverse()
        for move, shape in solution:
            print(f'Move: {move}')
            #for row in shape:
                #print(row)
            #print()
    else:
        print("Failed")
