from sys import stdin, stdout

def find(n,s,p,t):
    count = 0
    M = 3 * p
    for m in t:
        if m >= M:
            count +=1
        else:
            r = (m - p)/2
            if r >= p-1:
                count +=1
            elif s > 0:
                if r == p-2 and p-2 >= 0:
                    s -= 1
                    count +=1
    return count

T = int(stdin.readline())
for x in xrange(T):
    case = stdin.readline().split()
    N = int(case[0])
    S = int(case[1])
    p = int(case[2])
    t = [int(i) for i in case[3:]]
    print >> stdout, "Case #%d: %d" % (x+1,find(N,S,p,t))

