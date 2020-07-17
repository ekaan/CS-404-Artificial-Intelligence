from ortools.linear_solver import pywraplp

def addVariables(solver,board):

    squares = {}

    for i in  range( len(board) ):
        for j in range( len(board[0]) ):

            if board[i][j][0] != 'X':
                squares[(i,j)] = solver.IntVar(0,1,"Var %d,%d" % (i,j))

    return squares

def addConstraints(solver, squares, board):
    for i in range(len(board)):

        for j in range(len(board[0])):

            arr = []

            if board[i][j][0] != 'X':

                arr.append(squares[(i, j)])

                x_dec = i - 1

                while x_dec >= 0 and board[x_dec][j][0] != 'X':
                    arr.append(squares[(x_dec, j)])
                    x_dec -= 1

                x_inc = i + 1

                while x_inc <= len(board) - 1 and board[x_inc][j][0] != 'X':
                    arr.append(squares[(x_inc, j)])
                    x_inc += 1

                y_dec = j - 1

                while y_dec >= 0 and board[i][y_dec][0] != 'X':
                    arr.append(squares[(i, y_dec)])
                    y_dec -= 1

                y_inc = j + 1

                while y_inc <= len(board[0]) - 1 and board[i][y_inc][0] != 'X':
                    arr.append(squares[(i, y_inc)])
                    y_inc += 1

                constraint = solver.Constraint(1, 2)
                for sqr in arr:
                    constraint.SetCoefficient(sqr, 1)

def verticalConstraints(solver, squares, board):
    for i in range(len(board)):

        for j in range(len(board[0])):

            arr = []

            if board[i][j][0] != 'X':

                arr.append(squares[(i, j)])

                x_dec = i - 1

                while x_dec >= 0 and board[x_dec][j][0] != 'X':
                    arr.append(squares[(x_dec, j)])
                    x_dec -= 1

                x_inc = i + 1

                while x_inc <= len(board) - 1 and board[x_inc][j][0] != 'X':
                    arr.append(squares[(x_inc, j)])
                    x_inc += 1

                constraint = solver.Constraint(0, 1)
                for sqr in arr:
                    constraint.SetCoefficient(sqr, 1)

def horizontalConstraints(solver, squares, board):
    for i in range(len(board)):

        for j in range(len(board[0])):

            arr = []

            if board[i][j][0] != 'X':

                arr.append(squares[(i, j)])

                y_dec = j - 1

                while y_dec >= 0 and board[i][y_dec][0] != 'X':
                    arr.append(squares[(i, y_dec)])
                    y_dec -= 1

                y_inc = j + 1

                while y_inc <= len(board[0]) - 1 and board[i][y_inc][0] != 'X':
                    arr.append(squares[(i, y_inc)])
                    y_inc += 1

                constraint = solver.Constraint(0, 1)
                for sqr in arr:
                    constraint.SetCoefficient(sqr, 1)

def numConstraints(solver, squares, board):
    for i in range(len(board)):

        for j in range(len(board[0])):

            if board[i][j][0] == 'X' and board[i][j][1] != ' ':

                arr = []

                num = int(board[i][j][1])

                if i - 1 >= 0:
                    if board[i - 1][j][0] != 'X':
                        arr.append(squares[(i - 1, j)])

                if j - 1 >= 0:
                    if board[i][j - 1][0] != 'X':
                        arr.append(squares[(i, j - 1)])

                if i + 1 <= len(board) - 1:
                    if board[i + 1][j][0] != 'X':
                        arr.append(squares[(i + 1, j)])

                if j + 1 <= len(board[0]) - 1:
                    if board[i][j + 1][0] != 'X':
                        arr.append(squares[(i, j + 1)])

                constraint = solver.Constraint(num, num)
                for sqr in arr:
                    constraint.SetCoefficient(sqr, 1)

def main():

    solver = pywraplp.Solver('SolveSimpleSystem',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    myBoard = [['O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'X1', 'X '],
               ['O ', 'O ', 'X1', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'X1'],
               ['O ', 'X ', 'X ', 'X3', 'O ', 'O ', 'X ', 'O ', 'O ', 'O '],
               ['O ', 'O ', 'X ', 'O ', 'O ', 'O ', 'O ', 'X0', 'O ', 'O '],
               ['O ', 'O ', 'O ', 'O ', 'O ', 'X ', 'O ', 'O ', 'O ', 'O '],
               ['O ', 'O ', 'O ', 'O ', 'X ', 'O ', 'O ', 'O ', 'O ', 'O '],
               ['O ', 'O ', 'X0', 'O ', 'O ', 'O ', 'O ', 'X2', 'O ', 'O '],
               ['O ', 'O ', 'O ', 'X ', 'O ', 'O ', 'X1', 'X ', 'X1', 'O '],
               ['X1', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'X ', 'O ', 'O '],
               ['X ', 'X ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ']]

    squares = addVariables(solver,myBoard)

    addConstraints(solver,squares,myBoard)
    verticalConstraints(solver, squares, myBoard)
    horizontalConstraints(solver, squares, myBoard)
    numConstraints(solver, squares, myBoard)

    result_arr = []

    for i in range( len(myBoard) ):
        for j in range( len(myBoard[0]) ):

            if (i,j) in squares:
                result_arr.append(squares[(i,j)])
    solver.Solve()
    for var in result_arr:
        print(var,"-" ,var.solution_value())

main()

'''
myBoard = [['O ','O ','O ','O ','O ','X1','O '],
           ['O ','O ','O ','X0','O ','O ','O '],
           ['O ','O ','O ','X1','X ','O ','O '],
           ['O ','X1','X ','X2','O ','O ','X1'],
           ['O ','O ','O ','O ','O ','O ','X1'],
           ['O ','O ','O ','X1','X1','O ','O '],
           ['X ','O ','O ','O ','O ','O ','O ']]

myBoard = [['O ','O ','O ','O ','O ','O ','X '],
           ['O ','O ','X4','O ','O ','O ','O '],
           ['X0','O ','O ','O ','X1','X ','O '],
           ['O ','O ','O ','X1','O ','O ','O '],
           ['O ','X ','X1','O ','O ','O ','X '],
           ['O ','O ','O ','O ','X ','O ','O '],
           ['X1','O ','O ','O ','O ','O ','O ']]
           
myBoard = [['O ','O ','O ','O ','O ','O ','O ','O ','X1','X '],
           ['O ','O ','X1','O ','O ','O ','O ','O ','O ','X1'],
           ['O ','X ','X ','X3','O ','O ','X ','O ','O ','O '],
           ['O ','O ','X ','O ','O ','O ','O ','X0','O ','O '],
           ['O ','O ','O ','O ','O ','X ','O ','O ','O ','O '],
           ['O ','O ','O ','O ','X ','O ','O ','O ','O ','O '],
           ['O ','O ','X0','O ','O ','O ','O ','X2','O ','O '],
           ['O ','O ','O ','X ','O ','O ','X1','X ','X1','O '],
           ['X1','O ','O ','O ','O ','O ','O ','X ','O ','O '],
           ['X ','X ','O ','O ','O ','O ','O ','O ','O ','O ']]


'''