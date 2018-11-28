def solve():
	line = input().split(' ')
	ls = [int(s) for s in line]
	R = ls[0]
	C = ls[1]
	W = ls[2]
	if ((W == C) or (W == 1)):
		return R*C 
	else:
		if (C%W == 0):
			plus = W - 1
		else:
			plus = W
		return R*((C//W) + plus)

T = int(input())

res = [solve() for i in range(0,T)]
for i in range(0,len(res)):
	print("Case #{}: {}".format(i+1, res[i]))
