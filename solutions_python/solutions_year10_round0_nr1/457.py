import sys

def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[1][:-2] + 'out', 'w')
	
	for case in range(1, int(infile.readline())+1):
		snappers, snaps = (int(number) for number in infile.readline().split())
		
		if (snaps+1)%(2**snappers)==0:
			state = "ON"
		else:
			state = "OFF"
		
		outfile.write("Case #%i: %s\n"%(case, state))

if __name__ == "__main__":
	main()