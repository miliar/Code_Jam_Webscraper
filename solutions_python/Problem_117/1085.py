# helper file function
def parselineint(f):
    mylist = f.readline().split()
    for xen in range(len(mylist)):
        mylist[xen] = int(mylist[xen])
    return mylist

# helper board functions
# n x m: n rows, m cols
# ninin: 0 to n-1. mimim:; 0 to m-1.
# any number x, you want to check that either row or column is at most x

def validrow(myboard, ninin, mimim):
    row = myboard[ninin]
    
    for square in row:
        if square > row[mimim]: # if any square greater, it wasn't cut by row
            return False
    return True

def validcol(myboard, ninin, mimim):
    for daninin in range(n):
        if myboard[daninin][mimim] > myboard[ninin][mimim]:
            return False
    return True

def solve(board):
    for ninin in range(n):
        for mimim in range(m):
            if not (validrow(board, ninin, mimim)\
                    or validcol(board, ninin, mimim)):
                return "NO"
    return "YES"

#############################

# get files
name = raw_input() # name of file without .in suffix
f = open(name+".in", 'r')
g = open(name+".out", 'w')

# get cases
cases = int(f.readline())
i = 0
while i < cases:
    # get n x m
    values = f.readline().split()
    n = int(values[0])
    m = int(values[1])
    
    # construct list of list of ints
    board = []
    for ninin in range(n):
        board.append(parselineint(f))
    # solve
    result = "Case #%d: " % (i+1) + solve(board)
    g.write(result + "\n")
    
    # progress
    i += 1
    #f.readline() # if blank line

f.close()
g.close()

###########################
