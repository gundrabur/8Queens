import multiprocessing
import matplotlib.pyplot as plt

class EightQueens:
    def __init__(self, num_queens):
        self.num_queens = num_queens

    def is_safe(self, board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(self, start_col):
        solutions = []
        board = [-1] * self.num_queens
        board[0] = start_col
        self._solve(board, 1, solutions)
        return solutions

    def _solve(self, board, row, solutions):
        if row == self.num_queens:
            solutions.append(list(board))
            return

        for col in range(self.num_queens):
            if self.is_safe(board, row, col):
                board[row] = col
                self._solve(board, row + 1, solutions)
                board[row] = -1

def plot_solution(solution):
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
    
    with multiprocessing.Pool() as pool:
        solutions = pool.map(solver.solve, range(num_queens))

    flattened_solutions = [sol for sublist in solutions for sol in sublist]
    print("Number of solutions:", len(flattened_solutions))
    for solution in flattened_solutions:
        print(solution)
        plot_solution(solution)
