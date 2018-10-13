from sys import stdin

def min_time(farm_cost, extra, targt,  current, cur_time):
	time_with_current = target/ current
	#import pdb;pdb.set_trace()
	time_to_farm =farm_cost/ current
	future_speed =extra +  current
	future_time = target/  future_speed
	future_time =future_time+ time_to_farm
	if future_time >=  time_with_current + 1e-10:
		return cur_time +  time_with_current
	return min_time(farm_cost, extra, target, future_speed, cur_time + time_to_farm)
	
	
test = int(stdin.readline())
for case in xrange(test):
	input = stdin.readline()
	input = input.split()
	farm_cost = float(input[0])
	extra = float(input[1])
	target = float(input[2])
	#print "you gave ", cost, extra, target
	cur_time = 0.0
	res = 0.0
	current = 2.0
	while True:
		time_with_current = target/ current	
		time_to_farm =farm_cost/ current
		future_speed =extra +  current
		future_time = target/  future_speed
		future_time =future_time+ time_to_farm
		if future_time >=  time_with_current + 1e-10:
			res =  cur_time +  time_with_current
			break
		current = future_speed
		cur_time += time_to_farm
	
		
	#print ans[0]/ans[1],".",

	print "Case #%d: %.15lf"%((case+1),res)
		
	