import sys
import string

def flip(s, i, k):
    if s[i:i+k] == '+'*k:
        return s
    result = s[:i]
    for j in xrange(k):
        result += '-' if s[j+i]=='+' else '+'
    result += s[i+k:]
    return result
    
def sunny(s):
    if s=='':
        return True
    t = [c=='+' for c in s]
    return all(t)
        
def tryflip(initial, k, seen, generation):
    if sunny(initial):
        return generation
    initial = string.strip(initial, "+")
    if initial in seen:
        if seen[initial]<generation:
            return 9999999
    seen[initial] = generation
    L = len(initial)
    if L<k:
        return 9999999
    options = [flip(initial, i, k) for i in xrange(0, L-k+1)]
    results = [tryflip(o, k, seen, generation+1) for o in options]
    return min(results)

T = int(sys.stdin.readline())
for n, testcase in enumerate(sys.stdin.readlines(), 1):
    initial, k = testcase.split(" ")
    k = int(k)
    r = tryflip(initial, k, {}, 0)
    if r==9999999:
        r = "IMPOSSIBLE"
    print "Case #"+str(n)+": "+str(r)
    
    