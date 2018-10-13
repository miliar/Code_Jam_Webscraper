cases = int(input())
for case in range(1, cases + 1):
	destination, horses = [int(data) for data in input().split()]
	others = []
	for horse in range(horses):
		position, speed = [int(data) for data in input().split()]
		others.append((position, speed))
	times = [(destination - position) / speed for position, speed in others]
	max_time = max(times)
	velocity = destination / max_time
	print("Case #{}: {:.6f}".format(case, velocity))
