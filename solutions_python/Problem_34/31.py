#!/usr/bin/pyton
import re
def findOcc(words,pat):
    r = words
    for i in xrange(len(pat)):
        r = recomputeWords(r,pat[i],i)
        if len(r)==0:return 0
    return len(r)

def recomputeWords(r,token,i):
    rr=[]
    for w in r:
        if w[i] in token:
            rr.append(w)
    return rr

def toPat(w):
    p = []
    inp = False
    t = '' 
    for i in xrange(len(w)):
        if w[i]=='(':
            inp = True
            t = ''
        elif w[i]==')':
            inp = False
            p.append(t)
        else:
            if inp:
                t = t+w[i]
            else:
                p.append(w[i])
    return p
if __name__ == "__main__":
    import sys
    (L,D,N) = map(int,sys.stdin.readline().split())
    words = []
    d = re.compile('[()]')
    for i in xrange(D):
        words.append(sys.stdin.readline().strip())
    for i in xrange(N):
      pat = toPat(sys.stdin.readline().strip())
      #print pat
      t = findOcc(words,pat)
      print "Case #%d: %d" %(i+1,t)

