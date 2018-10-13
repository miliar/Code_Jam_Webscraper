"""
Google Code Jam quals problem 1
May 7, 2010, 8:22pm

clicked 'A.small.in' and GCJ immediately crashed, chrome didn't even
download the input file.

```
Error: Server Error

The server encountered an error and could not complete your request.
If the problem persists, please report your problem and mention this 
error message and the query that caused it.
```
'report' links to http://code.google.com/appengine/community.html

"""
fname = "A-large.in"

def bulblit(l, k):
    pstop = lambda l: l.index(False) + 1 if False in l else len(l)
    ohsnap = lambda l: [not s if i < pstop(l) else s for i, s in enumerate(l)]
    """ simulates k flips. too slow for large k. """ 
    for i in range(k):
        l = ohsnap(l)
    return all(l)

def checkmod(N, k): 
    """ checks if the number of flips is right. not sure why this works :P """
    guess = lambda N: (1 << N) if N > 0 else 1
    return False if (k + 1) % guess(N) else True
        

if __name__ == "__main__":
    f = lambda N: [False] * N
    f = open(fname)
    l = f.readlines()
    T = int(l.pop(0))
    i = 1
    while len(l):
        N, k = map(int,l.pop(0).split())
        bulbon = checkmod(N, k)
        print "Case #" + str(i) + ":", "ON" if bulbon else "OFF"
        i += 1

