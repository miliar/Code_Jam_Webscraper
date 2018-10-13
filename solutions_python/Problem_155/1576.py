i = open('A-large.in', 'r')
o = open('o.txt', 'w')
t = int(i.readline())

for _ in range(t):
    a, b = i.readline().split()
    a = int(a)
    b = list(b)
    b = map(int, b)
    sb = []
    sb.append(b[0])
    for x in range(1,len(b)):
        sb.append(b[x]+sb[x-1])

    m = max([max((x+1)-sb[x],0) for x in range(len(sb))])
    o.write('Case #%d: %d\n' % (_+1,m))

o.close()
o.close()
    
    
