import sys

def main(argv):
	global TOTAL
	with open(argv) as inputFile:
		testcases = inputFile.readline()

		for t in range (0, int(testcases)):
			# print "Test case: "+str(t+1)

			inputs = inputFile.readline().split()
			farm = float(inputs[0])
			increment = float(inputs[1])
			goal = float(inputs[2])
			
			total = 0.0 

			rate = 2.0

			while True:
				time_goal = goal/rate
				time_goal_next = goal/(rate+increment)
				time_farm = farm/rate

				if (time_farm + time_goal_next) < time_goal: 
					rate += increment
					total += time_farm
				else:
					total += time_goal
					break

			# print "Time: "+str(total)
			# print "Case #"+str(t+1)+": "+str(time_total)
			with open('output.txt', 'a') as output:
				output.write("Case #"+str(t+1)+": "+str(total)+"\n")

if __name__ == "__main__":
	# main(sys.argv[1:])
	main("B-large.in")