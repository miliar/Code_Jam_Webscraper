f = open('B-large.in', 'r')
T = int(f.readline().strip())

for t in xrange(T):
    l1 = f.readline().strip().split(" ")
    n = int(l1[0])
    m = int(l1[1])
    
    c  = []
    for i in range(n):
        c.append(map(int, f.readline().strip().split(" ")))
    l = map(list, zip(*c))
    works = True
    for x in range(n):
        for y in range(m):
            k = c[x][y]
            left = right = bottom = top = 0
            
            if y < m-1:
                top = max(c[x][y:])
            if y > 0:
                bottom = max(c[x][:y]) 
            if x < n-1:
                right = max(l[y][x:])
            if x > 0:
                left = max(l[y][:x])
            
            if not (bottom <= k and top <= k) and not (left <= k and right <= k):
                works = False
                break
        if not works:
            break
        
    if works:
        res = "YES"
    else:
        res = "NO"
        
    s = "Case #%d: %s\n" % (t+1, res)
    with open("resultLarge.out", "a") as o:
        o.write(s)
