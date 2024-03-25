def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("\n")

def check_winner(board, player):
    
    for row in board:
        if all(spot == player for spot in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(all(spot != " " for spot in row) for row in board)

def get_move():
    while True:
        try:
            move = int(input("لطفا یک شماره از 1 تا 9 وارد کنید: "))
            if 1 <= move <= 9:
                return move - 1
            else:
                print("شماره باید بین 1 تا 9 باشد.")
        except ValueError:
            print("لطفا یک عدد وارد کنید.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        print(f"نوبت بازیکن {current_player}")
        row, col = divmod(get_move(), 3)
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("این خانه پر است. لطفا دوباره امتحان کنید.")
            continue
        if check_winner(board, current_player):
            print_board(board)
            print(f"بازیکن {current_player} برنده شد!")
            break
        if check_draw(board):
            print_board(board)
            print("بازی مساوی شد!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
