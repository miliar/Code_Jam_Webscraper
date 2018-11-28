def flip(s, i, k):
    for j in xrange(k):
        if s[i+j] == '-': s[i+j] = '+'
        else: s[i+j] = '-'

def minFlips(s, k):
    n = len(s)
    count = 0
    for i in xrange(n-k+1):
        if s[i] == '-':
            flip(s, i, k)
            count += 1
    for i in xrange(n-k+1, n):
        if s[i] == '-': return None
    return count

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1,t+1):
        s, k = raw_input().split()
        s = list(s)
        k = int(k)
        r = minFlips(s, k)
        if r == None:
            print "Case #%d: IMPOSSIBLE" % (i,)
        else:
            print "Case #%d: %d" % (i, r)
            
        
        
