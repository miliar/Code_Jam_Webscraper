
def solve(case):
	dest, num_other_horses = [int(x) for x in input().split(' ')]
	pos = [None for _ in range(num_other_horses)]
	speed = [None for _ in range(num_other_horses)]
	for i in range(num_other_horses):
		pos[i], speed[i] = [int(x) for x in input().split(' ')]

	max_time = max((dest-pos[i])/speed[i] for i in range(num_other_horses))

	ans_speed = dest/max_time

	print('Case #{}: {}'.format(case, ans_speed))


num_tests = int(input())

for t in range(num_tests):
	solve(t+1)