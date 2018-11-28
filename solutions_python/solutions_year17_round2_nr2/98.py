T = int(input())
for t in range(1,T+1):
    n,r,o,y,g,b,v = [int(s) for s in input().split(' ')]
    colors = 'ROYGBV'
    l = [r,o,y,g,b,v]
    d = []
    for i in range(6):
        if colors[i] in 'RYB':
            d.append((l[i],colors[i]))

    d = sorted(d, key=lambda x: -x[0])

    if d[0][0] > d[1][0]+d[2][0]:
        result = 'IMPOSSIBLE'
    else:
        result = ''
        for i in range(d[0][0]):
            if i < d[1][0]:
                result += d[1][1]
            if i >=d[0][0]-d[2][0]:
                result += d[2][1]
            result += d[0][1]


    print('Case #{}: {}'.format(t,result))
