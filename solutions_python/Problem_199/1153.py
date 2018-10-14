import sys

def flip(pancakes, k):
	pancakes = list(pancakes)
	flips = 0
	while(1):
		if '-' not in pancakes:
			return flips
		
		if k > len(pancakes):
			return "IMPOSSIBLE"
		
		#Chop off the + start of the row
		i = 0
		for c in pancakes:
			if c == '+':
				i+=1
			else:
				break
				
		chopped = pancakes[i:]
		if k > len(chopped):
			return "IMPOSSIBLE"
		
		# flip k chopped pancakes
		for i in range(k):
			if chopped[i] == '+':
				chopped[i] = '-'
			else:
				chopped[i] = '+'
				
		flips += 1
		pancakes = chopped
	
			

def run_case(case_params):
	case_params = case_params.strip().split(" ")
	pancakes = case_params[0]
	k = int(case_params[1])
	return flip(pancakes, k)
	
def main():
	input = open(sys.argv[1], 'rb').readlines()
	number_of_cases = int(input[0])
	cases = input[1:number_of_cases+1]
	
	for i, case in enumerate(cases):
		ans = run_case(case)
		print "Case #%d: %s" % (i+1, ans)
		
if __name__ == "__main__":
	main()