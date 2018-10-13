#Problem Solution
def solve(data):
	distance = int(data[0])
	horse_count = int(data[1])
	slowest_travel_time = 0
	for i in range(horse_count):
		horse = input().split()
		horse_distance = int(horse[0])
		horse_speed = int(horse[1])
		horse_travel_time = (distance-horse_distance)/horse_speed
		if horse_travel_time > slowest_travel_time:
			slowest_travel_time = horse_travel_time
	annie_speed = distance/slowest_travel_time
	return annie_speed

T = int(input())  # reads in number of test cases

# Take input
for i in range(1, T + 1):
    print("Case #{}: {} ".format(i, solve((input().split()))))
    