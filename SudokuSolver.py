class Sudoku:

    def __init__(self):
        self.board = [["."]*9 for _ in range(9)]

    def __init__(self, inputBoard):
        if len(inputBoard) != 9 and len(inputBoard[0]) != 9:
            print("Invalid input size, try again!")
            return
        for i in range(9):
            for j in range(9):
                if inputBoard[i][j] not in [".",1,2,3,4,5,6,7,8,9]:
                    print("Invalid inputs in cells, try again!")
        self.board = inputBoard

    def solve(self):
        #self.printBoard()
        nextOpen = self.findNextOpen()
        if nextOpen == False: # Ie the puzzle is solved
            return self.board
        
        # If the puzzle isn't solved, ie has more whitespace
        for num in range(1,10,1): # For nums 1-9
            
            self.board[nextOpen[0]][nextOpen[1]] = num
            #self.printBoard()
            validBoard = self.checkValidBoard()
            #print(validBoard)
            if validBoard: # If this board with this edit is good
                solution = self.solve() # Finds the next open spot and keeps going
                if self.findNextOpen() == False: # Ie the puzzle is solved
                    return solution
            self.board[nextOpen[0]][nextOpen[1]] = "." # If its not solved, then we keep trying
    
    # Finds the next open square, On^2 brute force
    def findNextOpen(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    return [i,j]
        return False # If there's no open squares left, return False (ie none open)

    # Checks the rows, cols, and 3x3 squares for validity (ie no dupes)
    def checkValidBoard(self):
        # Check the rows
        for i in range(9):
            seenThisRow = set()
            for j in range(9):
                if self.board[i][j] != "." and self.board[i][j] in seenThisRow:
                    return False
                seenThisRow.add(self.board[i][j])
        
        # Check the cols:
        for j in range(9):
            seenThisCol = set()
            for i in range(9):
                if self.board[i][j] != "." and self.board[i][j] in seenThisCol:
                    return False
                seenThisCol.add(self.board[i][j])
        
        # Check the 3x3 squares
        for topLeftI in range(0, 9, 3):
            for topLeftJ in range(0, 9, 3):
                seenThisSquare = set()
                for i in range(topLeftI, topLeftI+3, 1):
                    for j in range(topLeftJ, topLeftJ+3, 1):
                        if self.board[i][j] != "." and self.board[i][j] in seenThisSquare:
                            return False
                        seenThisSquare.add(self.board[i][j])

        return True

    def printBoard(self):
        for row in self.board:
            print(row)
        print()

#myBoard = Sudoku()
'''
inputBoard1 = [[1,5,".",".",6,2,".",7,9],
               [2,7,".",9,".",".",6,5,"."],
               [".",".",".",4,".",7,".",1,"."],
               [".",".",1,".",".",3,7,2,"."],
               [7,".",8,".",".",".",9,".",5],
               [".",6,2,7,9,5,1,".","."],
               [".",".",".",6,3,".",2,9,"."],
               [".",2,".",".",1,9,".",6,"."],
               [9,4,".",".",".",".",".",".","."]]
'''
inputBoard2 = [[".",".",".",".",".",2,".",5,"."],
               [7,".",".",".",".",8,9,".",6],
               [1,9,".",5,".",".",".",".",4],
               [6,".",9,".",4,".",".",".",5],
               [".",".",".",".",".",9,7,".","."],
               [8,4,".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."],
               [".",2,".",".",1,".",".",".","."],
               [4,".",1,".",".",".",".",8,"."]]
myBoard = Sudoku(inputBoard2)
myBoard.solve()
myBoard.printBoard()