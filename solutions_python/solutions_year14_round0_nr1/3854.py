import sys

def solve(b,c,d,e):
    count = 0
    if b[d] == c[e]:
        return 'Bad magician!'
    else:
        for i in range(0,4):
            for j in range(0,4):
                if b[d][i] == c[e][j]:
                    count = count+1
                    res = b[d][i]
        if count == 0:
            return 'Volunteer cheated!'
        else:
            if count == 1:
                return res
            else:
                return 'Bad magician!'
            


f = open('input.txt','r')
o = open('Output.txt','w')
cases  = int(f.readline())

for num in range(1,cases+1):
    x = 0
    y = 0
    board1 = []
    board2 = []
    
    x = int(f.readline())
    for i in range(0,4):
        board1.append(f.readline().strip().split())

    y = int(f.readline())
    for i in range(0,4):
        board2.append(f.readline().strip().split())
        
    o.write("Case #" + repr(num) + ": " + solve(board1,board2,x-1,y-1)+"\n")

f.close()
o.close()
