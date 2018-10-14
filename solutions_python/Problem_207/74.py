t = int(raw_input())

def ryb(R, r, Y, y, B, b):
    if (r < y):
        return ryb(Y, y, R, r, B, b)
    if (y < b):
        return ryb(R, r, B, b, Y, y)
    d = y + b - r
    if d < 0:
        return 'IMPOSSIBLE'
    return (R+Y)*(y-d) + (R+Y+B)*d + (R+B)*(b-d)

s = "RGOBYV"
for case in xrange(t):
    # N r ry y yb b rb
    a = map(int, raw_input().split())
    ans = ryb('R', a[1], 'Y', a[3], 'B', a[5]) 
    print "Case #{case:d}: {ans:s}".format(case=case+1, ans=ans)

    #for i in xrange(3):
    #    if a[i+1] + a[i+4] == n and a[i+1] == a[i+4]:
    #        ans = s[(i*2) : (i*2+2)] * a[i+1]
    #    print "Case #{case:d}: {ans:s}\n".format(case=case, ans=ans)



