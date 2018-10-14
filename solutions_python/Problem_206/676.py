def solve(D, horses):
	maxTime = 0
	for horse in horses:
		time = (D-horse[0])/horse[1]
		maxTime = max(maxTime, time)
	return float(D)/maxTime


if __name__ == '__main__':
	T = int(input().strip())
	for i in range(T):
		D, N = map(int, input().strip().split(' '))
		horses = []
		for j in range(N):
			k, s = map(float, input().strip().split(' '))
			horses.append((k, s))
		sol = solve(D, horses)
		print('Case #{}: {}'.format(i+1, sol))