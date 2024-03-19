# 8-puzzle

8-puzzle is a Python project implementing various search algorithms to solve the classic 8-puzzle problem efficiently. The project provides implementations of Breadth-First Search (BFS), Depth-First Search (DFS), and A* Search algorithms with both Manhattan and Euclidean distance heuristics. The 8-puzzle problem involves arranging tiles numbered from 1 to 8 in a 3x3 grid, with one tile missing, to reach the goal state. 8-puzzle includes visualization of the solution path and metrics such as expanded nodes and elapsed time for each algorithm.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Algorithms](#algorithms)

## Introduction

The 8-puzzle problem is a classic problem in the field of artificial intelligence and computational problem-solving. It serves as a fundamental example for understanding various search algorithms and heuristic methods.

8-puzzle aims to provide a comprehensive toolkit for solving the 8-puzzle problem using different search algorithms and heuristics, allowing users to compare their performance and understand their strengths and limitations.

## Features

- Solve the 8-puzzle problem using Breadth-First Search (BFS), Depth-First Search (DFS), and A* Search algorithms.
- Implement both Manhattan and Euclidean distance heuristics for A* Search.
- Visualize the solution path and explore metrics such as expanded nodes and elapsed time for each algorithm.
- Check solvability of input puzzles to ensure valid inputs.
- Easy-to-use interface with clear instructions for running the project.

## Algorithms

### Breadth-First Search (BFS)

BFS explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

### Depth-First Search (DFS)

DFS explores as far as possible along each branch before backtracking.

### A* Search

A* Search combines the advantages of BFS and DFS by using a heuristic function to guide the search towards the most promising paths.


