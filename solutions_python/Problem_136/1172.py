def solveB():
	fileIn = open("in.txt", "r")
	lines = [line.strip() for line in fileIn]
	fileIn.close()
	
	fileOut = open("out.txt", "w")
	
	
	T = int(lines[0])
	count = 0
	i = 1
	while count < T:
		nums = lines[i].split(" ")
		C = float(nums[0])
		F = float(nums[1])
		X = float(nums[2])
		i += 1
		count += 1
		result = "Case #%i: %s\n" % (count, solve(C, F, X))
		print result
		fileOut.write(result)
	
	fileOut.close()
		
def solve(C, F, X):
	
	best = X / 2
	timeWithBuying = 0
	rate = 2
	while timeWithBuying <= best:
		best = min([best, timeWithBuying + X / rate])
		timeWithBuying += C / rate
		rate += F
	return best

solveB()