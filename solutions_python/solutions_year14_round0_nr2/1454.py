from decimal import *
def solve (cur_rate, time):
	while True:
		if (goal/cur_rate + time)<=(goal/(cur_rate + rate) + cost/cur_rate + time): 
			return goal/cur_rate + time
		time = time + cost/cur_rate
		cur_rate = cur_rate + rate

def main():
	getcontext().prec = 7
	T = input()
	for x in range(T):
		global cost, rate, goal
		cost, rate, goal = [ float(i) for i in raw_input().split()]
		print "Case #"+str(x+1)+": " + ("%.7f" % solve(2.000000, 0.000000))
main();