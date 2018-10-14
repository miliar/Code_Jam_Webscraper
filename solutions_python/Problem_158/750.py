import sys

input = file(sys.argv[1]).readline

def solution(y):
    o = y[0]
    w = y[1]
    h = y[2]
    if w*h%o != 0:
        return 'RICHARD'
    if o == 1:
        return 'GABRIEL'
    if o == 2:
        return 'GABRIEL'
    if o == 3:
        if w == 1 or h == 1:
            return 'RICHARD'
        else:
            return 'GABRIEL'
    if o == 4:
        if w <=2 or h <= 2:
            return 'RICHARD'
        else:
            return 'GABRIEL'

for case in range(int(input())):
	y = [int(z) for z in input().strip().split(' ')]
	print "Case #%d: %s " % (case+1, solution(y))
