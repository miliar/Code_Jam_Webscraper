import sys

def getByS(b):
    return (b-2)/3+2

def getByNS(b):
    return (b-1)/3+1

n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline()
    line = line[:-1].split()
    scores = []
    for l in line:
        scores.append(int(l))
    n = scores[0]
    s = scores[1]
    p = scores[2]
    ans = 0
    scores = scores[3:]
    scores.sort()
    scores.reverse()
    for score in scores:
        nss = getByNS(score)
        #print score,nss
        if nss >= p:
            ans = ans + 1
            #print "-->+1"
        elif s > 0 and score > 1:
            ss = getByS(score)
            #print '\t',score,ss
            s = s - 1
            if ss >= p:
                ans = ans + 1
                #print "--> +1"
    output = 'Case #'+str(i+1)+': '+str(ans)
    print output
