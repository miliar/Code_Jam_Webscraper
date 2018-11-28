def movesToAbsorb(p,t):
    if (p > t):
        return (p+t,0)
    mA = movesToAbsorb(p+p-1, t)
    return (mA[0], mA[1]+1)

def numMoves(size, start, motes):
    j = 0
    moves = 0
    if (size == 1):
        return len(motes)
    if (start >= len(motes)):
        return 0
    t = movesToAbsorb(size, motes[start])
    return min(t[1] + numMoves(t[0],start+1, motes), 1 + numMoves(size, start+1, motes))

f = open('A-small-attempt2.in','r')
g = open('A-small.out','w')
a = f.read()
b = a.split('\n')
d = ""

cases = (int)(b[0])

for i in range(cases):
    info = b[i*2+1].split(' ')
    size = (int)(info[0])
    num = (int)(info[1])
    motes = []
    m = b[(i+1)*2].split(' ');
    for j in range(num):
        motes.append((int)(m[j]))
    motes.sort()
    

    g.write("Case #"+(str)(i+1)+": " + (str)(numMoves(size,0,motes)) + "\n")

movesToAbsorb(2,100)

f.close()
g.close()
