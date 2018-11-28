fi = open('A-large (2).in','r')
fo = open('out.txt','w')

n = int(fi.readline().split()[0])
for i in range(n):
    a,b=map(int,fi.readline().split())
    m = []
    for y in range(a):
        m.append(list(fi.readline().strip('\n')))

    for y in range(a-1):
        for x in range(b-1):
            if m[y][x] == '#' and m[y+1][x] == '#' and m[y][x+1] == '#' and m[y+1][x+1] == '#':
                m[y][x]='/'
                m[y][x+1] = '\\'
                m[y+1][x] = '\\'
                m[y+1][x+1] = '/'
    fo.write('Case #%d:\n' % (i+1))
    t=True
    for y in range(a):
        for x in range(b):
            if(m[y][x]=='#'):
                t=False
                break
    if t != True:
        fo.write('Impossible\n')
    if t:
        for y in range(a):
            for x in range(b):
                fo.write(m[y][x])
            fo.write('\n')
fo.close()
