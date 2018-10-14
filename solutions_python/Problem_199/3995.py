import sys
import pdb

f = open("input.txt")
def input():
    return f.readline()

def invert(S):
    s1 = ""
    for i in S:
        if i == "+":
            s1 += "-"
        else:
            s1 += "+"
    return s1

def happy(S):
    for i in S:
        if i == '-':
            return False
    return True

def process(i, S, k):
    if k > len(S):
        print "Case #%d: IMPOSSIBLE!" % i
        return
    cache = dict()
    def bfs(s1):
        best = None
        if s1 in cache:
            return cache[s1]
        cache[s1] = None
        for l in xrange(0, len(s1)-k+1):
            s2 = s1[:l] + invert(s1[l:l+k]) + s1[l+k:]
            if happy(s2):
                best = 1
            else:
                done = bfs(s2)
                if done:
                    if not best:
                        best = done + 1
                    else:
                        best = min(best, done + 1)
                    #return done
        cache[s1] = best
        return best
    if happy(S):
        print "Case #%d: 0" % i
        return
    done = bfs(S)
    if done is None:
        print "Case #%d: IMPOSSIBLE" % i
    else:
        print "Case #%d: %d" % (i, done)

T = int(input())
for i in xrange(T):
    S, k = input().split()
    k = int(k)
    process(i+1, S, k)
