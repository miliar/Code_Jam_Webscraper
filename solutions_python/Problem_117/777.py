import sys

def solve_lawn(infile):
    n_row, n_col = map(int, infile.readline().strip().split(" "))
    
    lawn = []
    for i in range(n_row):
        rowvals = map(int, infile.readline().strip().split(" "))
        lawn.append( rowvals )
    #[[1,2,3],
    # [7,8,9]]

    transposed_lawn = transpose(lawn)

#For every cell:
# in some direction (four directions? two directions? TWO DIRECTIONS),
# it must be the max.
#Construct the transpose of evey grid, then you can just query on the row
    for i in range(n_row):
        for j in range(n_col):
            if not isMax(i,j,lawn,transposed_lawn):
                return "NO"
    return "YES"
    
def isMax(row,col,lawn,transposed_lawn):
    num = lawn[row][col]
    return (max(lawn[row]) == num or max(transposed_lawn[col]) == num)
    
def transpose(lawn):
    n_row = len(lawn)
    n_col = len(lawn[0])
    new_lawn = []
    for i in range(n_col):
        new_row = []
        for j in range(n_row):
            new_row.append( lawn[j][i] )
        new_lawn.append( new_row  )
    return new_lawn

if __name__=="__main__":
    infile = open(sys.argv[1],'r')
    outfile = open('output','w')
    
    t = int(infile.readline().strip())
    for i in range(t):
        result = solve_lawn(infile)
        string = "Case #%d: %s\n" % (i+1, result)
        print string[:-1]
        outfile.write(string)
