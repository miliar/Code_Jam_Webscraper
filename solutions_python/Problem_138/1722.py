import math
import re
f = open('D-large.in', 'r')
wf = open('outputDlarge.out', 'w')
t = f.readline()
print t
for k in range(int(t)):
    str1 = f.readline()
    n = int(str1)
    str1 = f.readline()
    p1 = re.split(' |, |\*|\n',str1)
    p1.pop(-1)
    p1 = [float(i) for i in p1]
    p1.sort()
    str1 = f.readline()
    p2 = re.split(' |, |\*|\n',str1)
    p2.pop(-1)
    p2 = [float(i) for i in p2]
    p2.sort()
    p3 = []
    for i in range(n):
        p3.append(['A',float(p1[i])])
        p3.append(['B',float(p2[i])])
    p3.sort(key=lambda j: j[1])
    p4 = list(p1)
    p5 = list(p2)
    p6 = list(p3)

    dw = 0
    for i in range(n):
        if p3[0][0] == 'A':
            p3.remove(['B',p2.pop(-1)])
            p1.remove(p3.pop(0)[1])
        else:
            p2.remove(p3.pop(0)[1])
            p3.remove(['A',p1.pop(0)])
            dw += 1

    w = 0
    while len(p6) != 0:
        if p6[-1][0] == 'A':
            p6.pop(-1)
            p4.pop(-1)
            p6.remove(['B',p5.pop(0)])
            w += 1
        else:
            ind = p6.index(['A',p4[-1]])
            p6.remove(['A',p4.pop(-1)])
            p5.remove(p6.pop(ind)[1])

    print k+1, dw, w



    wf.write('Case #'+str(k+1)+': '+str(dw)+' '+str(w)+'\n')



f.close()
wf.close()
