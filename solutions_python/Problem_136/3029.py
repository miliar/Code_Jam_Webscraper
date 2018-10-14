import sys

def solve():
	c, f, x = map(float, raw_input().split(' '))
	cur_speed = 2
	total_time = 0
	while x / cur_speed > c / cur_speed + x / (cur_speed+f):
		total_time += c / cur_speed
		cur_speed += f
	total_time += x / cur_speed
	return str(total_time)

probs = int(raw_input())
for i in range(probs):
	result = solve()
	print ("Case #%d: " % (i+1)) + result