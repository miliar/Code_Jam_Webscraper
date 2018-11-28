def isValid(pattern,rows,cols):
    for i in range(rows):
        for j in range(cols):
            #select each element in turn
            possible_col=True
            for k in range(rows):
                if pattern[i][j] < pattern[k][j]:
                    possible_col=False
                    break
            possible_row=True
            for k in range(cols):
                if pattern[i][j] < pattern[i][k]:
                    possible_row=False
                    break
            if not (possible_col or possible_row):
                return False
    return True

def show(grid):
    for row in grid:
        print row
    print ""

tests = int(raw_input())
i = 0
out = open('output.txt','w')
while i<tests:
    i+=1
    pattern = []
    n,m=raw_input().strip().split()
    n = int(n)
    m = int(m)
    for j in range(n):
        pattern.append([int(x) for x in raw_input().strip().split()])
    if isValid(pattern,n,m):
        out.write("Case #"+str(i)+": YES\n")
    else:
        out.write("Case #"+str(i)+": NO\n")