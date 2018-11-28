# Problem B

##Problem
##
##Alice and Bob have a lawn in front of their house, shaped like an N metre by M metre rectangle. Each year, they try to cut the lawn in some interesting pattern. They used to do their cutting with shears, which was very time-consuming; but now they have a new automatic lawnmower with multiple settings, and they want to try it out.
##
##The new lawnmower has a height setting - you can set it to any height h between 1 and 100 millimetres, and it will cut all the grass higher than h it encounters to height h. You run it by entering the lawn at any part of the edge of the lawn; then the lawnmower goes in a straight line, perpendicular to the edge of the lawn it entered, cutting grass in a swath 1m wide, until it exits the lawn on the other side. The lawnmower's height can be set only when it is not on the lawn.
##
##Alice and Bob have a number of various patterns of grass that they could have on their lawn. For each of those, they want to know whether it's possible to cut the grass into this pattern with their new lawnmower. Each pattern is described by specifying the height of the grass on each 1m x 1m square of the lawn.
##
##The grass is initially 100mm high on the whole lawn.
##
##Input
##
##The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing two integers: N and M. Next follow N lines, with the ith line containing M integers ai,j each, the number ai,j describing the desired height of the grass in the jth square of the ith row.
##
##Output
##
##For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either the word "YES" if it's possible to get the x-th pattern using the lawnmower, or "NO", if it's impossible (quotes for clarity only).case number (starting from 1) and y is the number of fair and square numbers greater than or equal to A and smaller than or equal to B.


# Get input file
input_fname = input("Input filename: ")
infile = open(input_fname, 'r')
# Set output file
output_fname = input_fname.replace("in", "out")
outfile = open(output_fname, 'w')

N = int(infile.readline().strip(" \n"))

for casenum in range(N):
    print("Case #", casenum+1, ": ", sep="", end="", file=outfile)

    N, M = [int(x) for x in infile.readline().strip(" \n").split(" ")]
    lawn = []
    for x in range(N):
        lawn.append([int(x) for x in infile.readline().strip(" \n").split(" ")])

    row_cuts = [max(lawn[x]) for x in range(N)]
    col_cuts = [max([lawn[x][y] for x in range(N)]) for y in range(M)]

    good_lawn = True
    for row in range(N):
        for col in range(M):
            if lawn[row][col] != min(row_cuts[row], col_cuts[col]):
                good_lawn = False

    if good_lawn:
        print("YES", end='', file=outfile)
    else:
        print("NO", end='', file=outfile)
        
    print("", file=outfile)
# end case loop

infile.close()
outfile.close()
