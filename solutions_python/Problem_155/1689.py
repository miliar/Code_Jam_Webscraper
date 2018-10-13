def solve():
	line = input().split(' ')
	ls = [int(s) for s in line[1]]
	tot = 0
	for i in range(0, len(ls)):
		if (sum(ls[:i])+tot) < i:
			tot = i - sum(ls[:i])
	return tot

T = int(input())

res = [solve() for i in range(0,T)]
for i in range(0,len(res)):
	print("Case #{}: {}".format(i+1, res[i]))
