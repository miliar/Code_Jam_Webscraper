from mpmath import *
mp.dps = 20
import sys
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out

t = int(inp.readline())

def print_case(case, result):
	print "Case #%d: %s" % (case, str(result))

for tc in xrange(t):
	freq = mpf(2)
	time = mpf(0)
	cost, farm, goal = [mpf(x) for x in inp.readline().split()]
	while True:
		time_to_next_farm = cost / freq
		time_to_goal = goal / freq
		time_to_goal_after_farm = goal/(freq+farm)
		
		if time_to_goal <= time_to_next_farm + time_to_goal_after_farm:
			print_case(tc+1,time+time_to_goal)
			break
		else:
			freq += farm
			time += time_to_next_farm
		
