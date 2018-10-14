def rainbow(n, r, o, y, g, b, v):
    if (r+o+v > n/2) or (o+y+g > n/2) or (g+b+v > n/2):
        return "IMPOSSIBLE"
    final = ['p']*n
    x = range(0,n,2)
    x.extend(range(1,n,2))
    ham1 = r+o+v
    ham2 = o+y+g
    ham3 = g+b+v
    maxham = max(ham1,ham2,ham3)
    if (ham1 == maxham):
        letters = 'V'*v + 'R'*r + 'O'*o + 'Y'*y + 'G'*g + 'B'*b
    elif (ham2 == maxham):
        letters =  'O'*o + 'Y'*y + 'G'*g + 'B'*b + 'V'*v + 'R'*r
    else:
        letters =  'G'*g + 'B'*b + 'V'*v + 'R'*r + 'O'*o + 'Y'*y
    for i in range(0,n):
        final[x[i]] = letters[i]
    return(''.join(final))


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, r, o, y, g, b, v = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, rainbow(n,r,o,y,g,b,v))


