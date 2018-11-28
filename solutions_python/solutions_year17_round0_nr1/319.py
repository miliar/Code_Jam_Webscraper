import sys

def solve():
	pancake, ksize = [x for x in sys.stdin.readline().split()]
	pancake = [x for x in pancake]
	ksize = int(ksize)
	cnt = 0
	for i in range(len(pancake)-ksize+1):
		if pancake[i] == '-':
			cnt += 1
			for j in range(i, i+ksize):
				pancake[j] = '+' if pancake[j] == '-' else '-'
		# print(pancake)
	return cnt if '-' not in pancake else 999999

ntest = int(sys.stdin.readline())
for i in range(ntest):
	ans = solve()
	print("Case #%d: %s"%(i+1, str(ans) if ans <= 1000 else "IMPOSSIBLE"))