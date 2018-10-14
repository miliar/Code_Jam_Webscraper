if __name__ == "__main__":
	with open("B-large.in", 'r') as inputf:
		outputf=open("B_out_large.out",'w')
		line=inputf.readline()
		line=line.rstrip('\n')
		test_num=int(line)
		
		for test in range(test_num):

			cookie_gen = float(2)
			time = float(0)

			line = inputf.readline()
			line = line.rstrip('\n')
			info = line.split(' ')

			C = float(info[0])
			F = float(info[1])
			X = float(info[2])

			while True:
				farm_time = C/cookie_gen
				next_win_time = X/(cookie_gen+F)
				curr_win_time = X/cookie_gen

				if curr_win_time < farm_time+next_win_time:
					time = time + curr_win_time
					break

				time = time + farm_time
				cookie_gen = cookie_gen+F

			result = "Case #%d: %.7f" % (test+1, time)
			outputf.write(result)

			if test!=test_num-1:
				outputf.write('\n')




