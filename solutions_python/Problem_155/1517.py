import sys

input = file(sys.argv[1]).readline

def solution(x, y):
    add = 0
    num = y[0]
    for i in range(1,x+1):
        if num < i:
            add += i-num
            num = i
        num += y[i]
    return add

for case in range(int(input())):
	val = input().strip().split(' ')
	x = int(val[0])
	y = [int(z) for z in val[1]]
	print "Case #%d: %d " % (case+1, solution(x, y))
