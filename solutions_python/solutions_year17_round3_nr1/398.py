entrada = open("A-large.in")
salida = open("a.out", 'w')
from math import pi
for case in xrange(1, int(entrada.readline())+1):
    salida.write("Case #" + str(case) + ": ")
    n, k = map(int, entrada.readline().split())
    pancakes = [map(int, entrada.readline().split()) for _ in xrange(n)]
    pancakes2 = [(i[0]*i[0]*pi, i[1]*2*i[0]*pi) for i in pancakes]
    pancakes2.sort(key = lambda x: x[1])
    if k == 1:
        area = max(i[0]+i[1] for i in pancakes2)
        salida.write(str(area)+"\n")
        continue
    subp = pancakes2[-k::]
    subp.sort()
    area1 = sum(i[1] for i in subp) + subp[-1][0]
    subp = pancakes2[-(k-1)::]
    subp2 = pancakes2[:-(k-1)]
    subp2.sort()
    subp.append(subp2[-1])
    subp.sort()
    area2 = sum(i[1] for i in subp) + subp[-1][0]
    salida.write(str(max(area1, area2))+"\n")
