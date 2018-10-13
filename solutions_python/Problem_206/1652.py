import sys
import copy

def solve():
	t = int(sys.stdin.readline())

	for i in range(t):
		out = sys.stdin.readline().split(" ")
		destination = int(out[0])
		num_horses = int(out[1])
		horses = []

		for j in range(num_horses):
			out = sys.stdin.readline().split(" ")
			horses.append( (int(out[0]), int(out[1])) )

		horses = sorted(horses, key=lambda x: x[0])
		ans = round(get_answer(horses, destination), 6)
		print("Case #{}: {}".format(i+1, ans))
		

def get_answer(horses, destination):
	horses2 = copy.deepcopy(horses)
	curr_horse = horses.pop(0)
	curr_loc = curr_horse[0]
	curr_speed = curr_horse[1]
	time = float(0)

	while horses:
		temp_horse = horses.pop(0)
		temp_loc = temp_horse[0]
		temp_speed = temp_horse[1]
		if temp_speed != curr_speed:
			x = (temp_loc-curr_loc) / (curr_speed-temp_speed)
			if x > 0 and ( ((temp_speed*x) + temp_loc) <= destination):
				curr_loc = (temp_speed*x) + temp_loc
				curr_speed = temp_speed
				time += x

	if curr_loc < destination:
		time += (destination-curr_loc) / curr_speed
	
	return destination/time

solve()


