#!/bin/python2

f = open('A-large.in', 'r')
g = open('A-small-practice.out', 'w')
n = int(f.readline())
for i in range(n):
    st = f.readline()
    [maxshy, a] = st.split()
    s = 0
    fr = 0
    for k in range(int(maxshy)):
        s += int(a[k])
        fr = max(fr, k + 1 - s)
    sout = 'Case #' + str(i + 1) + ': ' + str(fr) + '\n'
    g.write(sout)
f.close()
g.close()
