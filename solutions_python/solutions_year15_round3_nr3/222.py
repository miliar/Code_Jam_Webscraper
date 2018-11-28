import sys
input = file(sys.argv[1]).readline


def solution(x,y):
    d = x[1]
    v = x[2]
    add = []
    if y[0] != 1:
        z = y[0]-1
        i = 0
        while z!=0:
            add.append(1<<i)
            z = z>>1
            i += 1
    s = sum(add)
    for i in xrange(1,len(y)):
        if s >= v:
            return len(add)
        s += y[i-1]
        while s+1 < y[i]:
            add.append(s+1)
            s += add[-1]
    s += y[-1]
    while s < v:
        add.append(s+1)
        s += add[-1]
    return len(add)


for case in range(int(input())):
	x = [int(num) for num in input().strip().split(' ')]
	y = [int(num) for num in input().strip().split(' ')]
	print "Case #%d: %d " % (case+1, solution(x,y)) 
