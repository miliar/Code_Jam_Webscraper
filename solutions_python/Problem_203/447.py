def fixRowsFwd(inp):
    op = []
    for row in inp:
        oprow = []
        c = '?'
        for char in row:
            if char == '?':
                oprow.append(c)
            else:
                c = char
                oprow.append(c)
        op.append(oprow)
    
    return op

def fixRowsBwd(inp):
    op = []
    for row in inp:
        oprow = []
        c = '?'
        for k in range(len(row)-1,-1,-1):
            if row[k] == '?':
                oprow.insert(0,c)
            else:
                c = row[k]
                oprow.insert(0,c)
        op.append(oprow)
    
    return op

#s = fixRowsBwd(fixRowsFwd(t))
#print s

def fixEmptyRowsDownward(inp):
    op = [['']*len(inp[0]) for k in range(len(inp))]
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if i == 0:
                op[i][j] = inp[i][j]
            elif inp[i][j] == '?':
                op[i][j] = op[i-1][j]
            else:
                op[i][j] = inp[i][j]
    return op

def fixEmptyRowsUpward(inp):
    op = [['']*len(inp[0]) for k in range(len(inp))]
    for i in range(len(inp)-1,-1,-1):
        for j in range(len(inp[0])):
            if i == len(inp)-1:
                op[i][j] = inp[i][j]
            elif inp[i][j] == '?':
                op[i][j] = op[i+1][j]
            else:
                op[i][j] = inp[i][j]
    return op
#f =  fixEmptyRowsDownward(fixEmptyRowsUpward(s))
#print f


def solve(inp):
    s = fixRowsBwd(fixRowsFwd(inp))
    f =  fixEmptyRowsDownward(fixEmptyRowsUpward(s))
    op = ""
    for row in f:
        for char in row:
            op+=char
        op+="\n"
    return "\n"+op.strip()




import sys
filename = sys.argv[1]
f = open(filename, "r")
s = f.read()
f.close()


lines = s.split("\n")
lines = [l.strip() for l in lines]
T = int(lines[0])
j=1
for i in range(1,T+1,1):
	l = lines[j]
	R = int(l.split(" ")[0])
	IN = lines[j+1:j+1+R]
	j+=R+1
	ans = solve(IN)
	print "Case #"+str(i)+": "+ans