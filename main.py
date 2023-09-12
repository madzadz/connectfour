def create_board(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * len(row))


def is_valid_move(board, col):
    return board[0][col] == ' '


def drop_disc(board, col, player):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = player
            break


def check_win(board, player):
    for row in range(6):
        for col in range(7):
            if (
                    col + 3 < 7 and board[row][col] == player and
                    board[row][col + 1] == player and
                    board[row][col + 2] == player and
                    board[row][col + 3] == player
            ):
                return True
            if (
                    row + 3 < 6 and board[row][col] == player and
                    board[row + 1][col] == player and
                    board[row + 2][col] == player and
                    board[row + 3][col] == player
            ):
                return True
            if (
                    row + 3 < 6 and col + 3 < 7 and
                    board[row][col] == player and
                    board[row + 1][col + 1] == player and
                    board[row + 2][col + 2] == player and
                    board[row + 3][col + 3] == player
            ):
                return True
            if (
                    row - 3 >= 0 and col + 3 < 7 and
                    board[row][col] == player and
                    board[row - 1][col + 1] == player and
                    board[row - 2][col + 2] == player and
                    board[row - 3][col + 3] == player
            ):
                return True
    return False


def main():
    rows, cols = 6, 7
    board = create_board(rows, cols)
    player_turn = 'X'

    while True:
        print_board(board)
        col = int(input(f"Player {player_turn}, choose a column (0-6): "))

        if col < 0 or col >= cols or not is_valid_move(board, col):
            print("Invalid move. Try again.")
            continue

        drop_disc(board, col, player_turn)

        if check_win(board, player_turn):
            print_board(board)
            print(f"Player {player_turn} wins!")
            break

        if all(row.count(' ') == 0 for row in board):
            print_board(board)
            print("It's a draw!")
            break

        player_turn = 'O' if player_turn == 'X' else 'X'


if __name__ == "__main__":
    main()