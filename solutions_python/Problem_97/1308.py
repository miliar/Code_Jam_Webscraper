def rotatesort(s):
    l = len(s)
    t = s
    m = int(t)
    smallest = t

    for i in range(l-1):
        new = t[1:] + t[0]
        t = new
        n = int(t)
        if n < m:
            m = n
            smallest = t

    return smallest

t = int(raw_input(''))
for qq in range(1, t+1):
    s = raw_input().split()
    a = int(s[0])
    b = int(s[1])
    ndigits = len(s[0])

    m = {}

    for i in range(a, b+1):
        t = rotatesort(str(i))
        if t in m:
            m[t] = m[t]+1
        else:
            m[t] = 1
    
    count = 0
    for (t,n) in m.items():
        if n == 1:
            continue
        count = count + (n * (n - 1)) / 2

    print 'Case #' + str(qq) + ': ' + str(count)
