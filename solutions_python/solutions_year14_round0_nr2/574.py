from sys import stdin

def main():
	T = int(stdin.readline())
	for t in xrange(1,T+1):
		C,F,X = (float(v) for v in stdin.readline().strip().split(" "))
		curr_rate = 2.0
		best_time = X/curr_rate
		purchased_time = 0.0
		while True:
			purchased_time += C/curr_rate
			curr_rate += F
			new_time = purchased_time + X/curr_rate
			if new_time > best_time:
				break
			best_time = new_time
		print "Case #%d: %.7f"%(t,best_time)




if __name__ == '__main__':
	main()