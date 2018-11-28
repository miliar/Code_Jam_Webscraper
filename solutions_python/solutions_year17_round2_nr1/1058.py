t = int(input())
cases = []
for c in range(t):
	info = [int(i) for i in input().split()]
	tmp = []
	for x in range(info[1]):
		tmp.append([int(i) for i in input().split()])
	cases.append([info, tmp])

for i, case in enumerate(cases):
	info = case[0]
	horses = case[1]
	road_len = info[0]
	time_max = 0
	for horse in horses:
		horse_time = (road_len - horse[0]) / horse[1]
		if horse_time > time_max:
			time_max = horse_time
	result = road_len / time_max
	print("Case #{}: {}".format(i+1, result))