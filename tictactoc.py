import random
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
player= "X"
winner = None
gamerun= True

def printBoard(board):
    print(board[0] +" | " +board[1] + " | " + board[2])
    print("----------") 
    print(board[3] +" | " +board[4] + " | " + board[5])
    print("----------") 
    print(board[6] +" | " +board[7] + " | " + board[8])       
def playerinput(board):
    a = int(input("Enter a number 1-9: ") )
    if a>=1 and a<=9 and board[a-1]=="-":
        board[a-1] = player
    else : 
        print(" OOPs player is already in that spot")   


def horizontal(board):
    global winner
    if board[0] == board[1] == board[2] == board[0] != "-"  : 
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] == board[3] != "-"  : 
        winner = board[3]
        return True    
    elif board[6] == board[7] == board[8] == board[6] != "-"  : 
        winner = board[6]
        return True
def vertical(board):
    global winner
    if board[0] == board[3] == board[6] == board[0] != "-"  : 
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] == board[1] != "-"  : 
        winner = board[1]
        return True    
    elif board[2] == board[5] == board[8] == board[2] != "-"  : 
        winner = board[2]
        return True 
def diagonal(board):
    global winner
    if board[0] == board[4] == board[8] == board[0] != "-"  : 
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] == board[2] != "-"  : 
        winner = board[2]
        return True    

def checkwin(board) :
    global gamerun
    if horizontal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gamerun = False

    elif vertical(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gamerun = False

    elif diagonal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gamerun = False

def tie(board):
    global gamerun
    if "-" not in board:
        printBoard(board)
        print("It's a tie")
        gamerun = False


def switch():
    global player
    if player == "X":
        player ="O"
    else:
        player = "X"  
def computer(board):
    while player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch()


while gamerun:       

    printBoard(board) 
    playerinput(board)   
    
    checkwin(board)
    tie(board)
    switch()
    computer(board)
    checkwin(board)
    tie(board)