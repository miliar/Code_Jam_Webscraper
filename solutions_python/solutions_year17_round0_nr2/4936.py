def isTidy(k):
    snd = k % 10
    for i in range(0, len(str(k))-1):
        k = k / 10
        first = k % 10
        if first > snd:
            return False
        snd = first
    return True

def solve(k):
    while k > 1:
        if isTidy(k):
            return k
        k -= 1
    return 1
            
        

t = int(raw_input())
for i in xrange(1, t + 1):
    k = int(raw_input())
    print "Case #" + str(i) + ": " + str(solve(k))
