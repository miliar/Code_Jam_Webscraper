from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(1000000)

T = int(stdin.readline().strip())

lines = []
memos = {}

def cakes_from(s, c):
    string = ""
    for _ in range(c):
        if s & 1:
            string += "-"
        else :
            string += "+"
        s = s >> 1
    return string

def check(i, s, c, k):
    if s == 0:
        return 0
    elif (i, s, c, k) not in memos:
        memos[(i, s, c, k)] = -1
        flip = 0
        for j in range(k):
            flip += 1<<j
        flip = flip << i
        new_s = s ^ flip
        best = -1
        for j in range(c - (k-1)):
            maybe = check(j, new_s, c, k)
            if maybe == 0:
                best = maybe
                break
            elif maybe == -1 :
                pass
            elif best == -1 or maybe < best:
                best = maybe
        if best == -1:
            memos[(i, s, c, k)] = best
        else : 
            memos[(i, s, c, k)] = best + 1
##        print cakes_from(new_s, c), best + 1
    return memos[(i, s, c, k)]
            

for t in range(1, T+1):
    cakes, k = stdin.readline().strip().split()
    s = 0
    # convert cakes to an int: goal is to get s to be 0.
    for i, c in enumerate(cakes):
        if c == "-":
            s += 1<<i
##    print cakes_from(s, len(cakes)) , s
##    print 
    k = int(k)

    # find the best option by testing them all!
    best = -1
    for i in range(len(cakes) - (k-1)):
        maybe = check(i, s, len(cakes), k)
        if maybe == 0:
            best = maybe
            break
        if maybe == -1 : pass
        elif maybe < best or best == -1:
            best = maybe

    # record results
    if best == -1:
        lines.append("Case #%d: %s" % (t, "IMPOSSIBLE"))
    else :
        lines.append("Case #%d: %d" % (t, best))
    print lines[-1]


with open('googjama.txt', 'w') as outfile:
    outfile.write('\n'.join(lines))
