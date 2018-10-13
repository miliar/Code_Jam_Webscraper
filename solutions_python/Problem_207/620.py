def f(N,colors):
    s = []
    while True:
        res = ok2(N, colors)
        if res != False:
            return s + res
        colors[0] -= 1
        if colors[0] == -1:
            return False
        s.append(0)
        res = ok2(N, colors)
        if res != False:
            return s + res
        colors[1] -= 1
        colors[2] -= 1
        s.append(1)
        s.append(2)
        if -1 in colors:
            return False



def ok2(N,colors):
    if colors[0] == colors[1] + colors[2] - 1:
        return [1,0] * (colors[1]-1) + [1] + [0,2] * colors[2]
    return False

fin = open('b2.in')
fout = open('b2.out','w')
T = int(fin.readline())
for i in range(1, T+1):
    [N,R,_,Y,_,B,_] = [int(x) for x in fin.readline().split(' ')]
    m = list(reversed(sorted([('R',R),('Y',Y),('B',B)], key = lambda x: x[1])))
    l = [x[1] for x in m]
    ma = {}
    res = f(N, l)
    if res == False:
        res = 'IMPOSSIBLE'
    else:
        res = ''.join([m[x][0] for x in res])
    fout.write('Case #%s: %s\n' % (i, res))