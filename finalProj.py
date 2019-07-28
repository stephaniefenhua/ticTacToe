import random

class Player:
    letter = ''

    def __init__(self, name, number, gameboard):
        self.name = name
        self.number = number
        self.playBoard = gameboard
        self.board = gameboard.board
    
    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Player 1, do you want to be X or O?')
            letter = input()
    # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def makeMove(self, move):
        self.board[move] = self.letter

    def isWinner(self):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == self.letter and self.board[8] == self.letter and self.board[9] == self.letter) or # across the top
        (self.board[4] == self.letter and self.board[5] == self.letter and self.board[6] == self.letter) or # across the middle
        (self.board[1] == self.letter and self.board[2] == self.letter and self.board[3] == self.letter) or # across the bottom
        (self.board[7] == self.letter and self.board[4] == self.letter and self.board[1] == self.letter) or # down the left side
        (self.board[8] == self.letter and self.board[5] == self.letter and self.board[2] == self.letter) or # down the middle
        (self.board[9] == self.letter and self.board[6] == self.letter and self.board[3] == self.letter) or # down the right side
        (self.board[7] == self.letter and self.board[5] == self.letter and self.board[3] == self.letter) or # diagonal
        (self.board[9] == self.letter and self.board[5] == self.letter and self.board[1] == self.letter)) # diagonal

    def getPlayerMove(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.playBoard.isSpaceFree(int(move)):
            print(self.name + ', what is your next move? (1-9)')
            move = input()
        return int(move)

class Gameboard:
    def __init__(self):
        self.board = [' '] * 10

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

class Gameplay:
    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

    def takeTurns()

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    newBoard = Gameboard()
    player1, player2 = Player('Player 1', 1, newBoard), Player('Player 2', 2, newBoard)
    player1.letter, player2.letter = player1.inputPlayerLetter()
    newGame = Gameplay()
    turn = newGame.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player 1':
            # Player 1's turn.
            newBoard.drawBoard()
            move = player1.getPlayerMove()
            player1.makeMove(move)

            if player1.isWinner():
                newBoard.drawBoard()
                print('Player 1 has won.')
                gameIsPlaying = False
            else:
                if newBoard.isBoardFull():
                    newBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            newBoard.drawBoard()
            move = player2.getPlayerMove()
            player2.makeMove(move)

            if player2.isWinner():
                newBoard.drawBoard()
                print('Player 2 has won.')
                gameIsPlaying = False
            else:
                if newBoard.isBoardFull():
                    newBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not newGame.playAgain():
        break