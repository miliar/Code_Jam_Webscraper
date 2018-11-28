# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def expand(row,col,cake,dir,forward):
    if row<0 or col<0 or row>len(cake)-1 or col>len(cake[0])-1:
        return
    if dir == 0:

        if forward == 1:
            if cake[row][col] != '?':
                if col+1<len(cake[0]) and cake[row][col+1]=='?':
                    cake[row][col+1]=cake[row][col]
            expand(row, col+1, cake, dir, forward)
        else:
            if cake[row][col] != '?':
                if col-1 > -1 and cake[row][col-1] == '?':
                    cake[row][col-1] = cake[row][col]
            expand(row, col-1, cake, dir, forward)
    else:

        if forward == 1:
            if cake[row][col] != '?':
                if row+1<len(cake) and cake[row+1][col]=='?':
                    cake[row+1][col]=cake[row][col]
            expand(row+1,col,cake,dir,forward)
        else:
            if cake[row][col] != '?':
                if row-1>-1 and cake[row-1][col]=='?':
                    cake[row-1][col]=cake[row][col]
            expand(row-1,col,cake,dir,forward)

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
#    line = raw_input().split()
#    flip_str = line[0]
#    pan = line[1]

    rnc = raw_input().split()

    row = int(rnc[0])
    col = int(rnc[1])

    cake = []

    for _ in range(row):
        cake.append(list(raw_input()))

    nflag=True
    for r in range(row):
        if '?' in cake[r]:
            nflag = False
            break
    if nflag:
        print "Case #"+str(i)+":"
        for r in range(row):
            print "".join(cake[r])
        continue

    for r in range(row):
        expand(r, 0, cake, 0, 1)
        expand(r, col-1, cake, 0, -1)


    for c in range(col):
        expand(0,c,cake,1,1)
        expand(row-1,c,cake,1,-1)

    print "Case #"+str(i)+":"
    for r in range(row):
        print "".join(cake[r])