def cruise(total_distance, total_horses, positions, speeds):
	time = []
	for i in range(total_horses):
		t = (total_distance - positions[i]) / speeds[i]
		time.append(t)
	max_t = max(time)
	return total_distance / max_t


total = int(input())
t = 0
while t < total:
	t = t + 1
	distance, horses = [s for s in input().split(" ")]
	distance = int(distance)
	horses = int(horses)
	positions = []
	speeds = []
	for i in range(horses):
		position, speed = [q for q in input().split(" ")]
		position = int(position)
		speed = int(speed)
		positions.append(position)
		speeds.append(speed)
	result = cruise(distance, horses, positions, speeds)
	print("Case #%d: %f" %(t, result))