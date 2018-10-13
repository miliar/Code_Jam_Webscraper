i = open('D-small-attempt0.in', 'r')
o = open('o.txt', 'w')
t = int(i.readline())

for _ in range(t):
    x, r, c= i.readline().split()
    x = int(x)
    r = int(r)
    c = int(c)

    minrc = [(1,1),(1,2),(2,3),(3,4)]

    if ( r*c % x == 0 ):
        if minrc[x-1] <= (min(r,c),max(r,c)) :
            o.write('Case #%d: GABRIEL\n' % (_+1))
        else:
            o.write('Case #%d: RICHARD\n' % (_+1))
    else:
        o.write('Case #%d: RICHARD\n' % (_+1))
    

i.close()
o.close()
