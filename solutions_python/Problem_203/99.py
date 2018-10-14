t = input()
for icase in range(1,t+1):
    r,c = map(int,raw_input().split())
    o = []
    b = [raw_input().strip() for _ in range(r)]
    i,top,bot = 0,0,r-1
    while b[bot] == '?'*c:
        bot -= 1
    while b[top] == '?'*c:
        top += 1
    while top < bot:
        j = 0
        while b[top][j] == '?':
            j += 1
        row = b[top][j]*(j+1)
        for k in range(j+1,c):
            if b[top][k] == '?':
                row += row[-1]
            else:
                row += b[top][k]
        o.extend([row]*(top-i+1))
        top += 1
        i = top
        while b[top] == '?'*c:
            top += 1
    j = 0
    while b[top][j] == '?':
        j += 1
    row = b[top][j]*(j+1)
    for k in range(j+1,c):
        if b[top][k] == '?':
            row += row[-1]
        else:
            row += b[top][k]
    o.extend([row]*(r-i))
    print 'Case #%d:' % icase
    for row in o:
        print row
