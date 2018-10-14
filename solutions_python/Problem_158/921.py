def solve():
	ls = [int(x) for x in input().split(' ')]
	A = ls[1] * ls[2]
	if (A % ls[0] != 0):
		return 'RICHARD'
	elif (ls[0] > 2 * ls[1] or ls[0] > 2 * ls[2]):
		return 'RICHARD'
	elif (ls[0] == 4 and (ls[1] == 2 or ls[2] == 2)):
		return 'RICHARD'
	else:
		return 'GABRIEL'

T = int(input())

res = [solve() for i in range(0,T)]
for i in range(0,len(res)):
	print("Case #{}: {}".format(i+1, res[i]))
