from sys import stdin

def solve(N, W, L, r):
	r = sorted(r, reverse=True)
	#print (N, W, L, r)
	lr = len(r)
	
	cx, cy = 0, 0
	ans = []
	i = 0
	br = r[0][0]
	while i < lr and cx < W:
		while i < lr and cy < L:
			ans.append((cx, cy, r[i][1]))
			if i < lr - 1:
				cy += r[i][0] + r[i + 1][0]
			else:
				return ans
			i += 1
		cx += br + r[i][0]
		cy = 0
		br = r[i][0]
			
	return []

def main():
	T = int(stdin.readline())
	for Ti in xrange(T):
		N, W, L = map(int, stdin.readline().split(' '))
		r = map(int, stdin.readline().split(' '))
		for i in xrange(len(r)):
			r[i] = (r[i], i)
		ans = solve(N, W, L, r)
		ans = sorted(ans, key=lambda x: x[2])
		s_ans = []
		for i in xrange(len(ans)):
			s_ans.append(ans[i][0])
			s_ans.append(ans[i][1])
		ans = ' '.join(map(str, s_ans))
		print("Case #{}: {}".format(Ti + 1, ans))
		
if __name__ == '__main__':
	main()
