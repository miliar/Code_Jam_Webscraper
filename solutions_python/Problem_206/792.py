

if __name__ == "__main__":
	T = int(raw_input())
	for case in range(T):
		D, N = [int(t) for t in raw_input().strip().split()]
		# print "D, N = %d, %d" % (D, N)
		all_horse_time = []
		for horse in range(N):
			initial_position, speed = [int(t) for t in raw_input().strip().split()]
			# print "initial_position, speed = %d, %d" % (initial_position, speed)
			this_horse_time = (D - initial_position) / float(speed)
			all_horse_time.append(this_horse_time)
		longest_time = max(all_horse_time)
		answer = D / longest_time
		print "Case #%d: %f" % (case + 1, answer)
