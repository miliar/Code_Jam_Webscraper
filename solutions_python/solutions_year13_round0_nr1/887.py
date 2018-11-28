

vlines=[[(0,i),(1,i),(2,i),(3,i)] for i in range(4)]
hlines=[[(i,0),(i,1),(i,2),(i,3)] for i in range(4)]
dlines=[[(0,0),(1,1),(2,2),(3,3)],[(0,3),(1,2),(2,1),(3,0)]]

alllines=vlines+dlines+hlines

def state(x):
    result=""
    for line in alllines:        
        chars=[x[i][j] for (i,j) in line]        
        if all(c in ['X','T'] for c in chars):
            result="X won"
        if all(c in ['O','T'] for c in chars):
            result="O won"
    if result:
        return result
    else:
        for a in x:
            for b in a:
                if b=='.':
                    return "Game has not completed"
    return "Draw"


lines=open("A-large.in").read().split()

T=int(lines[0])

f=open("A-large.out","w")

for i in range(T):
    x=map(list,lines[i*4+1:i*4+5])
    f.write("Case #%d: "%(i+1)+state(x)+'\n')

f.close()    

    
