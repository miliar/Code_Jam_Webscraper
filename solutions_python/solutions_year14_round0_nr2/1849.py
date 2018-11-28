DEFAULT_PRODUCE = 2
FARM_PRODUCE = 0
FARM_COST = 0

def build_i_time(i):
	return FARM_COST / ((i - 1) * FARM_PRODUCE + DEFAULT_PRODUCE)

def build_time(count):
	return sum(map(build_i_time, range(1, count + 1)))

def process_case(case_number):
	input = raw_input()
	inputList = input.split(' ')
	inputList = map(float, inputList)

	global FARM_COST
	FARM_COST = inputList[0]
	global FARM_PRODUCE 
	FARM_PRODUCE = inputList[1]
	target = inputList[2]

	optimal_time = target / DEFAULT_PRODUCE 

	farms_to_use = 1
	while(True):
		total_produce = FARM_PRODUCE * farms_to_use + DEFAULT_PRODUCE
		wait_time = target / total_produce
		time = wait_time + build_time(farms_to_use)

		if time < optimal_time:
			optimal_time = time
			farms_to_use += 1
		else:
			break

	print "Case #{0}:".format(case_number), optimal_time

N = int(raw_input())

for i in xrange(0, N):
	process_case(i + 1)