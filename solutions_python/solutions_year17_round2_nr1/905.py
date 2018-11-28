T_cases = int(input())
for t_case in range(T_cases):
	[total_distance, num_horses] = [int(x) for x in input().split()]
	t = []
	for i in range(num_horses):
		[pos, speed] = [int(x) for x in input().split()]
		t.append((total_distance-pos)/speed)

	res = total_distance/max(t)
	print("Case #{}: {}".format(t_case+1, res))

	
	
