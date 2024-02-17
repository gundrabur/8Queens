#!/usr/bin/env python3

#
# 17.02.2024
# Christian Möller
#
 
import multiprocessing
import matplotlib.pyplot as plt
import time

class EightQueens:
    def __init__(self, num_queens):
        self.num_queens = num_queens

    def is_safe(self, board, row, col):
        """
        Checks if placing a queen at position (row, col) is safe.
        Args:
            board (list): Current state of the chessboard.
            row (int): Row index to check.
            col (int): Column index to check.
        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(self, start_col):
        """
        Finds solutions for the 8 queens problem starting from the specified column.
        Args:
            start_col (int): Starting column index for the first queen.
        Returns:
            list: List of solutions found.
        """
        solutions = []
        board = [-1] * self.num_queens
        board[0] = start_col
        self._solve(board, 1, solutions)
        return solutions

    def _solve(self, board, row, solutions):
        """
        Recursive helper function to find solutions for the 8 queens problem.
        Args:
            board (list): Current state of the chessboard.
            row (int): Current row being explored.
            solutions (list): List to store found solutions.
        """
        if row == self.num_queens:
            solutions.append(list(board))
            return

        for col in range(self.num_queens):
            if self.is_safe(board, row, col):
                board[row] = col
                self._solve(board, row + 1, solutions)
                board[row] = -1

def plot_solution(solution):
    """
    Plots a graphical representation of the chessboard with queens placed according to the solution.
    Args:
        solution (list): List representing the positions of queens on the board.
    """
    board_size = len(solution)
    board = [['.' for _ in range(board_size)] for _ in range(board_size)]
    for row, col in enumerate(solution):
        board[row][col] = 'Q'

    plt.figure(figsize=(board_size, board_size))
    plt.imshow([[1 if cell == 'Q' else 0 for cell in row] for row in board], cmap='binary')
    plt.xticks([])
    plt.yticks([])
    plt.show()

if __name__ == "__main__":
    num_queens = 8
    solver = EightQueens(num_queens)
    
    start_time = time.time()  # Start timing

    # Solve the problem in parallel using multiprocessing
    with multiprocessing.Pool() as pool:
        solutions = pool.map(solver.solve, range(num_queens))

    end_time = time.time()  # End timing
    execution_time = end_time - start_time

    # Flatten the list of solutions
    flattened_solutions = [sol for sublist in solutions for sol in sublist]
    print("Number of solutions:", len(flattened_solutions))
    print("Execution time:", execution_time, "seconds")
    
    # Print and plot each solution
    for solution in flattened_solutions:
        print(solution)
        #plot_solution(solution)
