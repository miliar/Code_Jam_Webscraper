#!/usr/bin/python


def cread(fd):
    return fd.readline().strip('\n')

def solve(fd):

    V0 = 0.5
    V1 = 1.0

    line = [ int(x) for x in cread(fd).split() ]
    L, t, N, C = line[:4]

    Ai0 = line[4:]

    # Now construct the full list...
    k,r = divmod(N,C)
    if r!=0:
        k += 1
    Ai = Ai0*k
    # Cut it to N starts
    Ai = Ai[0:N]

    # Calculate the Initial distance until the Warps are done
    D0 = t*V0

    # Advance until that moment arrives
    dist = 0.0
    dur = 0.0
    i = 0
    while dist<D0 and i<N:
        dist += Ai[i]
        dur += Ai[i]/V0
        i += 1

    if dist<D0:
        # Nothing to do with the boosters
        return dur
    elif dist>D0:
        # Add a fake star when D = D0
        i -= 1
        missing = dist-D0
        done = Ai[i] - missing
        dist = D0
        dur -= missing/V0
        Ai[i] = done
        i = i+1
        Ai.insert(i, missing)
    else:
        missing = None

    Rest = Ai[i:]

    # Now we can boost the biggest intervals...
    if missing is not None:
        Ai0.append(missing)
    Ai0 = list(set(Ai0))
    Ai0.sort(reverse=True)
    Boost = dict()
    for x in Ai0:
        Boost[x] = 0
    for j in xrange(len(Ai0)):
        h = Rest.count(Ai0[j])
        if h==0:
            continue
        if h>L:
            h = L
        Boost[Ai0[j]] = h
        L -= h
        if L<=0:
            break

    # Finally do the rest of the way
    for d in Rest:
        if Boost[d]>0:
            v = V1
            Boost[d] -= 1
        else:
            v = V0
        dist += d
        dur += d/v
        i += 1

    return dur




import sys

if len(sys.argv)<2:
    fd = sys.stdin
else:
    fd = open(sys.argv[1], 'r')

T = int(cread(fd))

for i in xrange(T):
    dur = solve(fd)
    print("Case #%d: %d" % (i+1, int(dur)))
    
fd.close()
    
    
    
        
        



