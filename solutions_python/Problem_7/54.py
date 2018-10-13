# Google CodeJam 2008
# Round 1B
# autor: HighEgg
import sys

input = open(sys.argv[1],'r')
ncases = int(input.readline())

sums3 = []
for i in range(3):
    for j in range(3):
	sums3.append((i,j,(3-i-j)%3))
sums2 = []
for i in range(3):
  sums2.append((i,(3-2*i)%3))



for icase in range(ncases):
    icase += 1
    n,A,B,C,D,x0,y0,M = map(int,input.readline().split())
    r = [[0]*3 for i in range(3)]
    X, Y = x0, y0
    r[X%3][Y%3] += 1
    for i in range(1,n):
	X = (A * X + B) % M
	Y = (C * Y + D) % M
	r[X%3][Y%3] += 1
    pairs = [(i,j) for i in range(3) for j in range(3)]
    total = 0
    for (i1,j1) in pairs:
	for (i2,j2) in pairs:
	    i3 = -(i1+i2)%3
	    j3 = -(j1+j2)%3
	    total += r[i1][j1]*r[i2][j2]*r[i3][j3]
	    if (i1,j1) == (i2,j2):
		total -= r[i1][j1]*r[i2][j2]
	    if (i3,j3) == (i2,j2):
		total -= r[i3][j3]*r[i2][j2]
	    if (i1,j1) == (i3,j3):
		total -= r[i1][j1]*r[i3][j3]
	    if (i1,j1) == (i2,j2) and (i2,j2) == (i3,j3):
		total += 2*r[i1][j1]
    total /= 6
    print "Case #%d: %d" % (icase,total)









