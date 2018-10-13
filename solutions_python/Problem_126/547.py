test = input()

def counter(s,i):
    c = 0
    for ch in s:
        t = ch not in "AEIOUaeiou"
        c = c + 1 if t else 0
        if c >= i:
            return True
    return False

def solve(a,b):
    count = 0
    la = len(a)
    for l in xrange(b,la+1):
        for start in xrange(la - l + 1):
            if counter(a[start:start+l] , b):
                count = count + 1
    return count

for case in xrange(1,test+1):
    a, b = raw_input().split()
    b = int(b)
    ans = solve(a,b)
    print "Case #" + str(case) + ": " + str(ans)