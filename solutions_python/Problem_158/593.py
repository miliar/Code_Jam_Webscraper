import math
import pdb


def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def print_ouput():
    lines = getInput("inputD.txt")
    no_cases = int(lines[0].strip())
    case = 1
    while (case<=no_cases):
        X, row, column = [int(y) for y in lines[case].strip().split()]
        sol = get_solution(X, row, column)
        print "Case #{0}: {1}".format(case, sol)
        case  += 1


def get_solution(X, row, column):
    #Let row be the smaller and column be the bigger dimension
    if row > column:
        row, column = column, row
    #Closed figures inclusive an empty space
    if X >= 8:
        return "RICHARD"
    #Check divisor
    if (row*column)%X != 0:
        return "RICHARD"
    #Corner cases
    if X in [1, 2]:
        return "GABRIEL"
    #overflow
    square_side_length = math.ceil(math.sqrt(X))
    if square_side_length > row or square_side_length > column:
        return "RICHARD"
    if X > row and X > column:
        return "RICHARD"

    #if 2 corners of a possible X-omino are missing and one of the dimensions matches the dimension of X-omino
    if X == 4 and row ==2 and column ==4:
        return "RICHARD"


    return "GABRIEL"

def get_highest_prime_factor(num):
    return
    

print_ouput()

