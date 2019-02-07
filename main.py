import time
import os

class ConsoleBoardDisplay:
    def display(self, spaces):
        s = spaces
        print(s[0], '|', s[1], '|', s[2], sep='')
        print('-----')
        print(s[3], '|', s[4], '|', s[5], sep='')
        print('-----')
        print(s[6], '|', s[7], '|', s[8], sep='')

class Board:
    def __init__(self, displayer):
        self.displayer = displayer
        self.spaces = [' '] * 9

    def display(self):
        self.displayer.display(self.spaces)

class Input:
    def getInput(self):
        return input()

def isValid(inp, board):
    try:
        inp = int(inp)
        return inp > 0 and inp <= len(board.spaces) and board.spaces[inp-1] == ' '
    except:
        return False

def findWinner(board):
    # check rows
    s = board.spaces
    if s[0] != ' ' and s[0] == s[1] and s[1] == s[2]:
        return s[0]
    if s[3] != ' ' and s[3] == s[4] and s[4] == s[5]:
        return s[3]
    if s[6] != ' ' and s[6] == s[7] and s[7] == s[8]:
        return s[6]

    # check columns
    if s[0] != ' ' and s[0] == s[3] and s[3] == s[6]:
        return s[0]
    if s[1] != ' ' and s[1] == s[4] and s[4] == s[7]:
        return s[1]
    if s[2] != ' ' and s[2] == s[5] and s[5] == s[8]:
        return s[2]

    # check diagonals
    if s[0] != ' ' and s[0] == s[4] and s[4] == s[8]:
        return s[0]
    if s[2] != ' ' and s[2] == s[4] and s[4] == s[6]:
        return s[2]

def play():
    b_gameover = False
    board_display = ConsoleBoardDisplay()
    board = Board(board_display)
    game_input = Input()
    curplayer = 'X'

    os.system('clear')       
    board.display()

    while not b_gameover:
        print("Enter a number 1-9: ", end='')
        s = game_input.getInput()
        b_valid = isValid(s, board)

        while not b_valid:
            print("Invalid choice")
            print("Enter a number 1-9: ", end='')
            s = game_input.getInput()
            b_valid = isValid(s, board)

        board.spaces[int(s)-1] = curplayer

        if curplayer == 'X':
            curplayer = 'O'
        else:
            curplayer = 'X'

        os.system('clear')       
        board.display()

        winner = findWinner(board)
        if winner != None:
            b_gameover = True
            print("Congrats {}, you win!".format(winner))
            input("Press enter to continue...")

    start()

def end():
    print("Goodbye!")
    time.sleep(1)

def start():
    os.system("clear")
    print("Welcome to TicTacToe!")
    answer = input("Would you like to play a game? Y/n: ")

    if answer in ['Y', 'y', '']:
        play()
    else:
        end()

start()
