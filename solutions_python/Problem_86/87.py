T  = int(raw_input())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a,b):
    return (a*b)/gcd(a,b)

for case in xrange(1,T+1):
    N,L,H = map(int, raw_input().split(" "))
    notes = map(int, raw_input().split(" "))
    ans = reduce(lcm,notes,notes[0])
    valid = False
    for i in xrange(L,H+1):
        pos= True
        for j in notes:
            if j%i == 0 or i%j==0:
                pass
            else:
                pos = False
                break
        if pos:
            valid = True
            ans =i
            break
    if valid:
        print "Case #%d: %d" %(case, ans)
    else:
        print "Case #%d: NO" %(case,)

