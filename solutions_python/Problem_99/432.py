import fileinput

infile = fileinput.input()

def r(fn='none', splt=True):
    '''r(fn=none, splt=True)
    Example: N, = r(long)
    S = r(str,splt=False)
    '''
    inp = infile.readline()
    if splt:
        inp = inp.split()
        return map(fn, inp)
    else:
        return fn(inp)

T, = r(long)

#gtoe = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

for t in range(T):
    A,B = r(int)
    F = r(float)
    f = len(F)
    P = [bin(i)[2:] for i in range(pow(2,A))]
    PRB = [1 for i in range(pow(2,A))]
    #print A,B,P
    for i in range(len(P)):
        diff = f - len(P[i])
        for n in range(diff):
            PRB[i] *= F[n]
        for n in range(len(P[i])):
            if P[i][n] == '0':
                PRB[i] *= F[diff + n]
            else:
                PRB[i] *= (1 - F[diff + n])
    #print PRB
    min = 100000000.0
    for c in range(1+A):
        cost = [0 for i in range(pow(2,A))]
        #print P
        for i in range(len(P)):
            cost[i] = c + (B - A + c) + 1
            if '1' in P[i][0:len(P[i])- c]:
                cost[i] += B + 1
            cost[i] *= PRB[i]
            #print i,P[i],"[",P[i][0:len(P[i])-c],"]", cost[i]
        if sum(cost) < min:
            min = sum(cost)
    #special case
    if A == B:
        sumcost = PRB[0] +  (sum(PRB[1:]) * (2 + B))
    else:
        sumcost = (B + 2) * sum(PRB)

    if sumcost < min:
        min = sumcost
    print "Case #%d: %0.6f"%(t+1, min)
