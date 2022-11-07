import random


def decide_startplayer():
    """
    Decide which Player starts
    """
    if random.randint(0, 1) == 0:
        return "Player One"
    else:
        return "Player Two"


def player_signinput():
    """
    Assign a sign to each Player. "X" or "O"
    """
    sign = ""
    while not (sign == "X" or sign == "O"):
        sign = input("Player One: Please input your Sign (X or O).").upper()
        if sign == "X":
            return "X", "O"
        else:
            return "O", "X"


def player_move():
    """
    Current Turn Move
    """
    while True:
        try:
            position = int(input("Please choose your position. It has to be between 1 and 9"))
        except:
            print("Please only enter Numbers between 1 and 9 and no Letters.")
        else:
            break

    return position


def place_marker(board, sign, posi):
    """
    Place Sign on Position
    """
    while True:
        if board[posi-1] == " ":
            board[posi-1] = sign
            break
        else:
            raise Exception("Only numbers between 1 and 9 are allowed. Or Field already in use.")
        continue


def show_board(board):
    """
    print board
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def win_check(board, mark):
    """
    decide if the player won
    """

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def replay():
    """
    Ask for Replaying
    """
    return input("Do you want to play again? Enter Yes or No.").lower().startswith("y")


def space_check(board, position):
    """
    check if the board[posi] is empty
    """

    return board[position] == " "


def full_board_check(board):
    """
    Check if board is full
    """
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Main Loop

while True:
    theBoard = [" "] * 10
    p1sign, p2sign = player_signinput()
    turn = decide_startplayer()
    print(turn + " will go first.")

    game_on = input("Are you ready to play? Yes or No.").upper().startswith("Y")

    while game_on:
        if turn == "Player One":
            show_board(theBoard)
            posi = player_move()
            place_marker(theBoard, p1sign, posi)
            if win_check(theBoard, p1sign) == True:
                show_board(theBoard)
                print("Congratulations P1 you won!")
                game_on = False
            else:
                if full_board_check(theBoard) == True:
                    print("Oh not! It's a tie")
                else:
                    show_board(theBoard)
                    turn = "Player Two"

        if turn == "Player Two":
            show_board(theBoard)
            posi = player_move()
            place_marker(theBoard, p2sign, posi)
            if win_check(theBoard, p2sign) == True:
                show_board(theBoard)
                print("Congratulations P2 you won!")
                game_on = False
            else:
                if full_board_check(theBoard) == True:
                    print("Oh not! It's a tie")
                else:
                    turn = "Player One"

        if not replay():
            break