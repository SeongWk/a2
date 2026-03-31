def make_board():
    return [' '] * 9


def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---|---|---")


def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None


def is_full(board):
    return ' ' not in board


def play():
    board = make_board()
    current = 'X'

    while True:
        print_board(board)
        print(f"\nPlayer {current}'s turn. Enter position (1-9): ", end="")

        try:
            pos = int(input()) - 1
        except ValueError:
            print("Invalid input. Enter a number 1-9.")
            continue

        if pos < 0 or pos > 8:
            print("Position must be between 1 and 9.")
            continue

        if board[pos] != ' ':
            print("That position is already taken.")
            continue

        board[pos] = current
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"\nPlayer {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        current = 'O' if current == 'X' else 'X'


if __name__ == '__main__':
    play()
