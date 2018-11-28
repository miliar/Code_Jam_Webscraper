__author__ = 'Victor'

fi = open('D-small-attempt2.in', 'r')
fo = open('OminousOmino.out', 'w')

t = int(next(fi))

for i in range(t):
    (X, R, C) = [int(x) for x in next(fi).strip().split(' ')]

    if X > 6:
        print('Case #%d: RICHARD\n' % (i+1))
    elif (R*C % X) != 0:
        fo.write('Case #%d: RICHARD\n' % (i+1))
    elif X == 2:
        fo.write('Case #%d: GABRIEL\n' % (i+1))
    elif X > C and X > R:
        fo.write('Case #%d: RICHARD\n' % (i+1))
    elif X == 2:
        fo.write('Case #%d: GABRIEL\n' % (i+1))
    elif (X//2 +1) > R or (X//2+1) > C:
        fo.write('Case #%d: RICHARD\n' % (i+1))
    else:
        fo.write('Case #%d: GABRIEL\n' % (i+1))



fi.close()
fo.close()
