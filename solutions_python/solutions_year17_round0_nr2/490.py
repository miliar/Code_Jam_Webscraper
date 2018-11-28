from sys import argv

def is_tidy(n):
	prev = "0"
	
	for c in n:
		if c < prev:
			return False
		prev = c
		
	return True
	
def solve(line):
	if is_tidy(line):
		return line
		
	prev = line[0]
	for i,c in enumerate(line[1:]):
		k = i + 1
		if c < prev:
			if line[k] != "0":
				return solve(line[:k-1] + str(int(line[k-1]) - 1) + "9" * len(line[k:]))
			else:
				j = k
				while j >= 0 and line[j] == "0":
					j -= 1
				if j == -1:
					return "9" * (len(line) - 1) 
				else:
					return solve((line[:j] + str(int(line[j]) - 1) + "9" * len(line[j+1:])).lstrip("0"))
		
		prev = c

if __name__ == "__main__":
	infile = open(argv[1], 'r')
	infile.readline()
	for (i,line) in enumerate(infile):
		print ("Case #%d: " + solve(line.strip('\n')).lstrip("0")) % (i+1)