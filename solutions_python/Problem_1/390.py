import sys

input_file = ""
output_file = ""
# Process All Arguments
def process_arguments():
	global input_file, output_file
	
	if len(sys.argv) != 3:
		exit(0)
		
	input_file = sys.argv[1]
	output_file = sys.argv[2]

# Check Dict:
#	if all values are 1, return True
#	if not all values are 1, return False
def CheckDict(dict):
	for v in dict.values():
		if (v == 0):
			return False
	return True

# Clear Dict:
#	Set all values to 0
def ClearDict(dict):
	for k in dict.keys():
		dict[k] = 0
		
def main():
	global input_file, output_file
	
	process_arguments()
	fd = open(input_file, 'r')
	ofd = open(output_file, 'w')
	N = int(fd.readline())
	
	# Case
	for n in range(N):
		# Search Engine
		S = int(fd.readline())
		sDict = {}
		for s in range(S):
			sName = fd.readline()
			sDict[sName] = 0
		
		# Quearies
		Q = int(fd.readline())
		T = 0;
		for q in range(Q):
			sName = fd.readline()
			sDict[sName] = 1
			if CheckDict(sDict):
				ClearDict(sDict)
				sDict[sName] = 1
				T += 1
		ofd.write("Case #%d: %d\n" % (n + 1, T))
	
	fd.close()
	ofd.close()
main()