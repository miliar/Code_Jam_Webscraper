def read():
	return raw_input().split(" ")

def test_case():
	C,F,X = map(float,read())
	#2 = cookied/min base
	#C = cost of a farm
	#F = cookies/sec of a farm
	#x = needed cookies
	
	#before farms:
	current_production = 2
	current_construction_time = 0
	
	while True:
		time_needed = current_construction_time + X/current_production
		
		time_to_construct_farm = C/current_production
		time_needed_after_farm = current_construction_time + time_to_construct_farm + X/(current_production+F)
		if time_needed_after_farm>time_needed:
			return time_needed
		
		current_production += F
		current_construction_time += time_to_construct_farm

def main():
	test_cases = int(raw_input())
	for i in range(test_cases):
		res = test_case()
		print "Case #%d: %s" % (i+1, res)

if __name__ == "__main__":
	main()
