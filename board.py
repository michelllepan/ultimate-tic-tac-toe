import numpy as np

class Board():

    @staticmethod
    def new_board() -> np.array:
        return np.zeros((9,9))
    
    @staticmethod
    def mark(board: np.array, local_board: tuple, pos: tuple, player: int) -> np.array:
        bi, bj = local_board
        i, j = pos
        new_board = board.copy()
        new_board[3*bi+i, 3*bj+j] = player
        return new_board
    
    @staticmethod
    def __check_win(board: np.array, player: int) -> bool:

        # check rows
        for row in range(3):
            if np.all(board[row,:] == player):
                return True

        # check columns
        for col in range(3):
            if np.all(board[:,col] == player):
                return True

        # check diagonals
        if (np.all(board.diagonal() == player) or 
            np.all(np.fliplr(board).diagonal() == player)):
            return True

        return False

    @staticmethod
    def check_local_win(board: np.array, local_board: tuple, player: int) -> bool:
        bi, bj = local_board
        local_squares = board[3*bi:3*(bi+1), 3*bj:3*(bj+1)]
        return Board.__check_win(local_squares, player)

    @staticmethod
    def check_global_win(board: np.array, player: int) -> bool:
        local_wins = np.zeros()
        for bi in range(3):
            for bj in range(3):
                won_local = Board.check_local_win(board, (bi, bj), player)
                local_wins[bi, bj] = player if won_local else 0
        return Board.__check_win(local_wins, player)

    @staticmethod
    def print_board(board: np.array) -> None:
        res = ""
        marks = {0: " ", 1: "X", 2: "O"}
        for row in range(9):
            row_squares = [marks[s] for s in board[row]]
            if row > 0 and row % 3 == 0:
                res += "-" * 21 + "\n"
            res += (" ".join(row_squares[0:3]) + " | " +
                    " ".join(row_squares[3:6]) + " | " + 
                    " ".join(row_squares[6:9]) + "\n")
        print(res)