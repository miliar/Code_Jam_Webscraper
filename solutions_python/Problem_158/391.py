import sys

f = open('D-small-attempt3.in')

T = int(f.readline())
for i in range(T):
    a = f.readline().split()
    X = int(a[0])
    R = int(a[1])
    C = int(a[2])
    if R>C:
        R, C = C, R
    flag = True
    if R*C%X:
        flag = False
    if X>R*2:
        flag = False
    if X==R*C and X>=3:
        flag = False
    if R==2 and C==X and X>=4:
        flag = False
    if not flag:
        print 'Case #{0}: RICHARD'.format(i+1)
    else:
        print 'Case #{0}: GABRIEL'.format(i+1)
    
