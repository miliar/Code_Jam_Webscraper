from collections import defaultdict


def alph(D):
    x = "".join(D)
    return set(x)

def findpos(x, ch):
    return set([i for i in range(len(x)) if x[i] == ch])


def sub(D, x, w):
    D = [u for u in D if len(u) == len(x)]

    score = 0
    for ch in w:
        if ch in alph(D):
            #print x, ch
            #print D
            if ch in x:
                D = [v for v in D if findpos(v, ch) == findpos(x, ch)]
            else:
                D = [v for v in D if findpos(v, ch) == findpos(x, ch)]
                score+=1
    return score

def calc(D, w):
    maxscore = -1
    ret = ""
    for x in D:
        score = sub(D, x, w)
        #print x, score
        if score > maxscore:
            #print " check", x
            maxscore = score
            ret = x

    return ret


T = int(raw_input())

for t in range(T):
    N, M = map(int, raw_input().split())

    D = []
    for i in range(N):
        w = raw_input()
        D.append(w)
    L = []
    for i in range(M):
        w = raw_input()
        L.append(w)

    #print D
    #print L

    print "Case #%d:" % (t+1),
    for w in L:
        print calc(D, w),
    print ""
 