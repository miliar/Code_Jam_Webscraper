from fractions import Fraction
f = open('A-large (1).in','r')
fo = open('A-large (1).out', 'w')
a = map(int,f.readline().split())[0]
for i in range(a):
    a,b,c = map(int,f.readline().split())
    if (c==100 and b<100) or (c==0 and b>0) or Fraction(b,100).denominator >a:fo.write('Case #%d: Broken\n' % (i+1))
    else: fo.write('Case #%d: Possible\n' %(i+1))
fo.close()
