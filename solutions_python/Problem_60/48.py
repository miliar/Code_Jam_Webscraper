INFILE = 'E:\\cj\\' + 'B' + '.in.txt'
OUTFILE = 'E:\\cj\\B' + '.out'

fin = open(INFILE, 'r')
lines = fin.readlines()
fin.close()

fout = open(OUTFILE, 'w')

def compat(x1, x2, v1, v2, B, N, T):
    d1 = B - x1
    time_to_catch = (x2 - x1)/float(v1 - v2)
    if d1 + time_to_catch*v1 >= B:
        return True
    
    

case = 0
cases = int(lines[0])
ptr = 1
for case in xrange(1, cases + 1):
    count = 0
    
    l = lines[ptr]
    ptr += 1
    N, K, B, T = map(int, l.split())
    X = map(int, lines[ptr].split())
    ptr += 1
    V = map(int, lines[ptr].split())
    ptr += 1

    impossible = False

    S = [0]*N # can it make to the barn?

    for chick in xrange(N - 1, -1, -1):
        x = X[chick]
        v = V[chick]
        time_to_barn = (B - x)/float(v)
        
        if time_to_barn <= T:
            S[chick] = 1

    if sum(S) < K:
        impossible = True
    else:
        # see how many swaps
        in_barn = 0
        pptr = N 
        tail = None
        laggards = 0
        while in_barn < K:
            pptr -= 1
            if S[pptr]:
                in_barn += 1
                count += laggards
            else:
                laggards += 1

    if impossible:       
        fout.write('Case #%d: IMPOSSIBLE\n' % (case))
    else:
        fout.write('Case #%d: %d\n' % (case, count))

fout.close()
    
