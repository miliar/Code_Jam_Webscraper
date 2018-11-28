import sys
table = [1, 4, 9, 121, 484]
t = 0
S = [0]
for i in xrange(1, 1001):
    if i in table:
        t+=1
    S.append(t)

sys.stdin = open('C-small.in')
f = file('C-small.out', 'w')
f.close()
sys.stdout = open('C-small.out', 'w')

case = 'Case #%d:'
T = input()
for t in xrange(1, T+1):
    line = raw_input()
    a = line.split()
    A, B = int(a[0]), int(a[1])
    print case%t, S[B]-S[A-1]
