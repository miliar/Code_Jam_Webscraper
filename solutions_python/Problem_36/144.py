import sys

w = "welcome to code jam"

inp = open(sys.argv[1])
lines = inp.readlines()
inp.close()

cache = []

for i in range(0,1000):
    cache += [[-1 for x in range(0,len(w))]]

N = int(lines[0])

def run(w_pos,l_pos,line):
    if cache[l_pos][w_pos] != -1:
        return cache[l_pos][w_pos]
    
    if w_pos == len(w): return 0
    
    next_pos = line.find(w[w_pos], l_pos)
    if next_pos  == -1:
        cache[l_pos][w_pos] = 0
    elif w_pos == len(w) - 1:
        cache[l_pos][w_pos] =  1 + run(w_pos, next_pos + 1, line)
    else:
        cache[l_pos][w_pos] = run(w_pos + 1, next_pos + 1, line) + run(w_pos, next_pos + 1, line)
    return cache[l_pos][w_pos]
    
def go(line):
    for i in range(0,1000):
        for j in range(0,len(w)):
            cache[i][j] = -1
    return run(0,0,line)


for i in range(0,N):
    print "Case #%d: %04d" % ((i+1), go(lines[i+1]) % 10000)

    
