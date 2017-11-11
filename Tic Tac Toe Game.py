# Defining Global variables to be used
board = (' ')*10
game_state = True
announce = ''

#For reseting the board
def reset_board, game_state
board = (' ')*10
game_state = True

#Creating a function for makng the board
def display_board():
    # Clear any output cell
clear_output()

# Printing the board
print "  "+board(7)+ "  |  "+board(8)+ "  |  " +board(9)+ "  "
print "--------------"
print "  "+board(4)+ "  |  "+board(5)+ "  |  " +board(6)+ "  "
print "--------------"
print "  "+board(1)+ "  |  "+board(2)+ "  |  " +board(3)+ "  "

#Defining a function for comparinf numbers for deciding Victory; will check horizontally
def win_check(board,player):
    if  (board(7) == board(8) == board(9) == player) or \
        (board(4) == board(5) == board(6) == player) or \
        (board(1) == board(2) == board(3) == player) or \
        (board(7) == board(4) == board(1) == player) or \
        (board(8) == board(5) == board(2) == player) or \
        (board(9) == board(6) == board(3) == player) or \
        (board(1) == board(5) == board(9) == player) or \
        (board(3) == board(5) == board(7) == player):
        return True
    else:
        return False

# Defining function to check if game is Tie or not
def full_board_check(board):
    if "  " in board(1:):
    return False
else:
    return True

#Defining function to get players input
def ask_player(mark):
    "asks player where to put the symbols and checks validity"
    global board
    req = 'Choose where to place:  ' + mark
    while True:
        try:
            choice = int(raw_input(req))
        except ValueError:
            print("Sorry, input a valid number between 0 and 9 only")
            continue

            if choice not in range (1,10):
                print("Sorry, please input numebr between 1-9")
                continue
                if board(choice) ==" ":
                    board(choice) = mark
                    break
                else:
                    print "Space is filled"
                    continue

#Gives a game state as output with help of input of player
def player_choice(mark):
    global board,game_state,announce

    #Set game annoucnement as blank game
    announce=''
    #Get imput from player
    mark=str (mark)
    #Validating the input now
    ask_player()

    #Check if he win
    if win_check(board,mark):
        clear_output()
        display_board()
        announce = mark + "         wins! Congrats"
        game_state = False

        #SHowing board
        clear_output()
        display_board()

        #Check for a tie game
        if full_board_check(board):
            announce= "Tie"
            game_state = False

            return game_state,announce

#Merging everything al together
def play_game():
    reset_board()
    global announce

    #Setting marking
    X = 'X'
    O = 'O'
    while True:
        #SHow board
clear_output()
display_board()

#Player X chance
game_state,announce = player_choice(X)
print announce
if game_state == False:
    break

    #Player O chance
    game_state,announce = player_choice(O)
    print announce
    if game_state == False:
        break

        #Ask for rematch
        rematch = raw_input('Will you play again, y/n')
        if rematch =='y':
            play_game()
        else:
            print "Thanks for playing game"

#Playing the game

play_game()