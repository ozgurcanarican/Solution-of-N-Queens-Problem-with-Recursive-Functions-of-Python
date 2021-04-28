import numpy as np

def recursion(board):
    
    for row in range(queens_number):
        for column in range(queens_number):
            if board[row][column] == 0:
                
                suitable_for_place_a_queen = True
                
                for square in range(queens_number):        #checks if there is any queen on the same row
                    if board[row][square] == 1:
                        suitable_for_place_a_queen = False
                        
                for square in range(queens_number):        #checks if there is any queen on the same column
                    if board[square][column] == 1:
                        suitable_for_place_a_queen = False
                        
                for horizontal in range(queens_number):    #checks if there is any queen on diagonal
                    for vertical in range(queens_number):
                        if board[horizontal][vertical] == 1:
                            if abs(horizontal - row) == abs(vertical - column):
                                suitable_for_place_a_queen = False
                                
                if suitable_for_place_a_queen:
                    board[row][column] = 1
                    recursion(board)
                    
                    if sum(sum(queen) for queen in board) == queens_number:
                        return board
                    
                    board[row][column] = 0
                    
    return board


while True:
    queens_number = int(input("Number of queens: "))
    while queens_number < 1:
        queens_number = int(input("Number of queens cannot be lower than 1. Reenter number of queens: "))
    while queens_number > 10:
        print("It may not find the solution when the number of queens higher than 10.")
        queens_number = int(input("Please enter a lower number: "))
        
    board = np.zeros([queens_number, queens_number], dtype = int).tolist()
    area_of_board = queens_number * queens_number
    
    recursion(board)
    
    for row in range(queens_number):
        board[row] = ["Q" if queen == 1 else "-" for queen in board[row]]
        
    print(np.array(board))
    
    
    new_calculation = str(input("Would you like to do a new calculation? (y/n): "))
    while new_calculation not in ["y", "n"]:
        new_calculation = str(input("Please enter 'y' or 'n': "))
    
    if new_calculation == "y":
        continue
    else:
        break
