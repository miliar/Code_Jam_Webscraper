'''
Created on May 30, 2015

@author: billyanhuang
'''
filename = 'B-small-attempt0.'

fin = open(filename + 'in', 'r')
fout = open(filename + 'out', 'w')

def update(X, param, source):
    if source[1] == X:
        param[4] += source[0]
    elif source[1] > X:
        param[1] = (param[1]*param[0] + source[1]*source[0])/(param[0] + source[0])
        param[0] += source[0]
    else:
        param[3] = (param[3]*param[2] + source[1]*source[0])/(param[2] + source[0])
        param[2] += source[0]
    return 

T = int(fin.readline())
for t in range(T):
    inp = fin.readline().split()
    N = int(inp[0])
    V = float(inp[1])
    X = float(inp[2])
    sources = []
    param = [0, X, 0, X, 0] #hR, hT, lR, lT, nR
    for i in range(N):
        inp = fin.readline().split()
        sources.append([])
        sources[i].append(float(inp[0]))
        sources[i].append(float(inp[1]))
        update(X, param, sources[i])
    
    #get difference in temperature
    param[1] -= X
    param[3] -= X
    param[3] = -param[3]
    if param[0] == 0 or param[2] == 0:
        param[0] = 0
        param[2] = 0
    else:
        if param[0]*param[1] < param[2]*param[3]:
            param[2] = param[0]*param[1]/param[3]
        else:
            param[0] = param[2]*param[3]/param[1]
    rate = param[0] + param[2] + param[4]
    
    if rate == 0:
        time = "IMPOSSIBLE"
    else:
        time = V/rate
    
    fout.write("Case #" + str(t+1) + ": " + str(time) + "\n")