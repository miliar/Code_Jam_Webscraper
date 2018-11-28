import sys

def main():
	lines = sys.stdin.readlines()
	first_line = lines[0].split()
	number_of_cases = int(first_line[0])
	
	for i in range(number_of_cases):
		split_line=lines[i+1].split()
		N=int(split_line[0])
		K=int(split_line[1])

		
		if K%(pow(2,N)) == pow(2,N) - 1:
			print 'Case #' + str(i+1) + ': ON'
		else:
			print 'Case #' + str(i+1) + ': OFF'
	
if __name__ == "__main__":
	main()