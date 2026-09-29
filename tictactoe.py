def print_board(board):
    """Prints the current game board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board, player):
    """Checks if the given player has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[cell] == player for cell in condition) for condition in win_conditions)

def check_draw(board):
    """Checks if the board is full (a draw)."""
    return all(cell in ['X', 'O'] for cell in board)

def tic_tac_toe():
    """Main function to run the game loop."""
    # Initialize the board with position numbers 1-9
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Enter a number from 1 to 9 to place your mark on the board.")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
            
            # Validate input bounds
            if move < 0 or move > 8:
                print("Invalid input. Please choose a number between 1 and 9.")
                continue
                
            # Check if the cell is already taken
            if board[move] in ['X', 'O']:
                print("That spot is already taken! Try another one.")
                continue
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Place the player's mark
        board[move] = current_player
        print_board(board)

        # Check for a winner
        if check_win(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check for a tie
        if check_draw(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
