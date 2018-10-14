import sys
sys.setrecursionlimit(10000)

def is_last(current_cookies, farm_increase, farm_cost, final):
	till_next = farm_cost/current_cookies
	next = current_cookies+farm_increase
	till_next_next = farm_cost/next
	return (final/current_cookies)<=(farm_cost/current_cookies)+(final/next) 


def find_time(current_cookies,  farm_cost, farm_increase, final, time =0):
	
	times_over = final/farm_cost
	if is_last(current_cookies, farm_increase, farm_cost, final):
		return (final/current_cookies)
	else:
		time = (farm_cost/current_cookies)
		return time + find_time(current_cookies+farm_increase,  farm_cost,farm_increase, final, time)

with open("B-small-attempt0.in") as inp:
	inp = inp.read().split("\n")
	with open("output", "w") as out:
		n = int(inp.pop(0))
		for i in xrange(n):
			do = [float(j) for j in inp.pop(0).split()]
			time = find_time(2.0, do[0], do[1], do[2])
			out.write("Case #%d: %.7f\n"%(i+1, time))