import sys

#input = open('test.in')
#input = open('A-small.in')
input = open('A-large.in')
#output = sys.stdout
#output = open('A-small.out','w')
output = open('A-large.out','w')
    
def myread():
    return input.readline().rstrip("\n\r")

def int_ize(an_array):
    return map(lambda x: int(x), an_array)

def main():
    n_cases = int(input.readline())
    
    case_no = 1
    while case_no <= n_cases:
        case_result = solve_case()
        output.write("Case #%d: %s\n" % (case_no, case_result))
        case_no+=1
        
def swap(row,j):
    newrow = ''
    if j > 0:
        newrow += row[:j]
    newrow += row[j+1] + row[j]
    if j + 2 < len(row):
        newrow += row[j+2:]
    return newrow
        
def rotate(matrix):
    ret_matrix = []
    length = len(matrix)
    for row in matrix:
        for i in range(length):
            for j in range(length-i-1):
                if row[j] != '.' and row[j+1] == '.':
                    #print "swapping %d:%d,%d %s,%s" % (j,j+1,row[j],row[j+1]) 
                    row = swap(row,j)
        ret_matrix.append(row)
                            
    return ret_matrix

def wins(color,k,matrix):
    length = len(matrix)
    # horizontal
    for row in matrix:
        for i in range(length-k+1):
            wins = True
            for j in range(i,i+k):
                if row[j] != color:
                    wins = False
                    break
            if wins:
                return True
            
    # vertical
    for i in range(length):
        for r in range(length-k+1):
            wins = True
            #print "Try range %d,%d" % (r,r+k)
            for j in range(r,r+k):
                if matrix[j][i] != color:
                    wins = False
            if wins:
                return True
    

    # diagonal \
    for i in range(length-k+1):
        for r in range(length-k+1):
            wins = True
            for j in range(k):
                #print "try %d,%d" % (r+j,i+j)
                if matrix[r+j][i+j] != color:
                    wins = False
            if wins:
                return True
            
    # diagnoal /
    for i in range(length):
        matrix[i] = matrix[i][::-1]
    for i in range(length-k+1):
        for r in range(length-k+1):
            wins = True
            for j in range(k):
                if matrix[r+j][i+j] != color:
                    wins = False
            if wins:
                return True    
    
    return False

def dump(board):
    for i in board:
        print i
    
def solve_case():
    (n,k) = int_ize(myread().split(" "))
    board = []
    for i in range(n):
        board.append(myread())
        
    board = rotate(board)
    #dump(board)
    
    red = wins('R',k,board)
    blue = wins('B',k,board)
    
    if red and blue:
        return "Both"
    elif red:
        return "Red"
    elif blue:
        return "Blue"
    else:
        return "Neither"

main()
