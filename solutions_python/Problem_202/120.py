# -------------------------
# Google Code Jam 2017
# Qualification Round
# 2017 April 8
# Brendan Wood
# brendanwood1989@gmail.com
# -------------------------
filename = 'D-small-attempt0'

# treat NxN grid as a chessboard
# consider '+' as bishops, 'x' as rooks, and 'o' as both bishops and rooks
# need to:
# 1) place as many bishops (+) on the board as possible, without attacking each other
# 2) place as many rooks (x) on the board as possible without attacking each other
# 3) upgrade any pieces unattacked by either bishops or rooks to 'o'
# for small input, can use the following arrangement of bishops:
#   + + + + + +
#   . . . . . .
#   . . . . . .
#   . . . . . .
#   . . . . . .
#   . + + + + .

def solve(N,M,models):

    new = []
    
    top_empty = [i+1 for i in range(N)]
    for model in models:
        top_empty.remove(model[2])
    
    # add 'bishops' to top row
    for col in top_empty:
        new.append('+ {} {}'.format(1,col))
    # add 'bishops' to bottom row
    for col in range(2,N):
        new.append('+ {} {}'.format(N,col))
    # add 'rooks' along diagonal
    for i in range(2,N+1):
        new.append('x {} {}'.format(i,i))
    # shift any overlapped rook to first column
    # upgrade model on top row, if not already upgraded
    upgraded = False
    for model in models:
        if   model[0] == 'x':
            if model[2] == 1:
                new.append('o 1 1')
                upgraded = True
                break
            new.remove('x {} {}'.format(model[2],model[2]))
            new.append('x {} {}'.format(model[2],1))
            new.append('o {} {}'.format(model[1],model[2]))
            upgraded = True
            break
        elif model[0] == 'o':
            if model[2] == 1:
                upgraded = True
                break
            new.remove('x {} {}'.format(model[2],model[2]))
            new.append('x {} {}'.format(model[2],1))
            upgraded = True
            break

    if not upgraded:
        if '+ 1 1' in new:
            new.remove('+ 1 1')
        new.append('o 1 1')
    
    if N == 1:
        y = 2
    else:
        y = 3*N-2
    z = len(new)
    return y, z, new
    
with open(filename+'.in') as f:
    data = f.read().splitlines()

f = open(filename+'.out', 'w')

T = int(data.pop(0))

for case in range(T):
    N,M = map(int,data.pop(0).split())
    models = []
    for m in range(M):
        t,r,c = data.pop(0).split()
        r = int(r)
        c = int(c)
        models.append((t,r,c))
    y, z, new = solve(N,M,models)
    f.write('Case #{}: {} {}\n'.format(case+1,y,z))
    for n in new:
        f.write(n+'\n')
        
f.close()