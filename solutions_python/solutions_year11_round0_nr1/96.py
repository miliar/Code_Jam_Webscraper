import sys

def mov(f, t, c):
    if abs(f - t) < c:
        return t
    else:
        if f < t :
            return f + c
        else:
            return f - c

for k in range(1, int(sys.stdin.readline())+1):
    line = sys.stdin.readline().rstrip().split()[1:]
    
    lb = 1
    lo = 1
    O = []
    B = []
    T = []
    for i in range(len(line)/2):
        a = line[2*i]
        b = int(line[2*i+1])
        T.append(a)        
        if a == 'O':
            O.append(b)
        else:
            B.append(b)
            
    time = 0
    while T <> [] and (O <> [] and B <> []):
        turn = T.pop(0)
    
        o = O[0]
        b = B[0]

       #print "time: ", time, ":", o, b, turn
        
        if turn == 'O':
            lb = mov(lb, b, abs(lo-o)+1)
            time += abs(lo-o) +1
            lo = o
            O.pop(0)
        else:
            lo = mov(lo, o, abs(lb-b)+1)
            time += abs(lb-b) +1
            lb = b
            B.pop(0)
            
    if T <> []:
        turn = T.pop()
        if turn == 'O':
            for o in O:
                time += abs(lo-o) +1
                lo = o
        else:
            for b in B:
                time += abs(lb-b) +1
                lb = b
            
        # print O, B
    print "Case #%d: %d"%(k, time)