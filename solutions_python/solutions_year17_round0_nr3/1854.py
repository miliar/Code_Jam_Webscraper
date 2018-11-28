


def solve(n, k):
    o = [False for i in range(n)]
    a = set()
    a.add((0,n-1))
    mid = None
    for i in range(k):
        (x,y) = max(a, key=lambda x: x[1] - x[0])
        a.remove((x,y))
        if (y - x) == 0:
            mid = x
        elif (y - x) == 1:
            mid = x
            a.add((y,y))
        else:
            mid = x + ((y - x) / 2)
            if mid > x:
                a.add((x,mid-1))
            if mid < y:
                a.add((mid+1,y))
        o[mid] = True
    l = 0
    r = 0
    i = mid
    while True:
        i += 1
        if i >= len(o) or o[i]:
            break
        else:
            l += 1
    i = mid
    while True:
        i -= 1
        if i < 0 or o[i]:
            break
        else:
            r += 1
    return (max(l,r), min(l,r))

i = 0
raw_input()
while True:
    i += 1
    try:
        a = raw_input()
    except EOFError:
        break
    (x,y) = solve(*[int(x) for x in a.split()])
    print ("Case #" + str(i) + ":"), x, y
#print solve(4,2)
#print solve(5,2)
#print solve(6,2)
#print solve(1000,1000)
#print solve(1000,1)
