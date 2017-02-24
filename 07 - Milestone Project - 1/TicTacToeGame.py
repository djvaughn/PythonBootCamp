import subprocess as sp


def clearShell():
    """This will clear the console"""
    tmp = sp.call('clear', shell=True)


def buildPlayer(playerName, symbol):
    """This will build a dictionary that contains both the name and symbol of the player"""
    playerDict = {'name': playerName, 'symbol': symbol}
    return playerDict


def buildBoard():
    """Creates a 3 by 3 size board/2d list"""
    board = [['*' for x in range(3)] for y in range(3)]
    return board


def printBoard(board):
    """Prints a formated version of the board.  It will first clear the console.  Then it will
    iterate over the board.  Print each symbol in the spot."""
    clearShell()
    print("  1 2 3 ")
    print("  - - - ")
    for row,i in zip(board, range(3)):
        print(str(i+1) + '|' + '|'.join([str(spot) for spot in row]) + "|\n  - - -")


def HorizontalWin(gameboard):
    """It will go row through row and determine if their is a winner"""
    for row in gameboard:
        # Checks
        if ('*' not in row and len(set(row)) == 1):
            return True, set(row)
        else:
            return False


def VerticalWin(gameboard):

    for i in range(3):
        column = [row[i] for row in gameboard]

        if ('*' not in column and len(set(column)) == 1):
            return True, set(column)

    return False


def DiagnolWin(gameboard):

    diagonal = [gameboard[i][i] for i in range(3)]

    reverseDiagnol = [gameboard[i][j] for i,j in zip(range(3), range(2,-1,-1))]

    if('*' in diagonal and '*' in reverseDiagnol):
        return False

    elif (len(set(diagonal)) == 1 or len(set(reverseDiagnol)) == 1):
        return True
    else:
        return False


def playerMoves(board, symbol, moveX, moveY):

    board[int(moveX)][int(moveY)] = str(symbol).upper()
    return board

def getPlayersMoves(playerDict):

    rawMove = input("[" + playerDict["name"] + "] What is your move(x,y)? ")
    moveX, moveY = rawMove.split(',')
    moveX = int(moveX) - 1
    moveY = int(moveY) - 1
    return moveX, moveY


def isGameOver(gameboard):

    return HorizontalWin(gameboard) or VerticalWin(gameboard) or DiagnolWin(gameboard)



def runGame(board, listOfPlayers):
    i = 0
    while not isGameOver(board):
        printBoard(board)
        moveX, moveY = getPlayersMoves(listOfPlayers[i % 2])
        board = playerMoves(board, listOfPlayers[i % 2]["symbol"], moveX, moveY)
        i = i +1
    print("Game Over")


def createPlayers():
    playerOne = input("Player 1: Name? ")
    playerTwo = input("Player 2: Name? ")
    return [buildPlayer(playerOne, 'X'), buildPlayer(playerTwo, 'O')]


def setGameUp():
    clearShell()
    print("Tic Tac Toe")
    board = buildBoard()
    listOfPlayers = createPlayers()
    runGame(board, listOfPlayers)

setGameUp()