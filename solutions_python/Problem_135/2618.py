import sys

i = open(sys.argv[1], 'r')
o = open(sys.argv[2], 'w')

T = int(i.readline())
for t in range(1, T + 1):
    r1 = int(i.readline())
    g1 = [i.readline().strip().split(),
          i.readline().strip().split(),
          i.readline().strip().split(),
          i.readline().strip().split()]
    r2 = int(i.readline().strip())
    g2 = [i.readline().strip().split(),
          i.readline().strip().split(),
          i.readline().strip().split(),
          i.readline().strip().split()]
    l = []
    p = g2[r2-1] + g1[r1-1]
    for el in p:
        if p.count(el) == 2:
            l.append(el)
    
    len_l = len(l)

    o.write('Case #' + str(t) + ': ')
    if len_l == 2:
        o.write(str(l[0]))
    elif len_l == 0:
        o.write('Volunteer cheated!')
    else:
        o.write('Bad magician!')
    o.write('\n')