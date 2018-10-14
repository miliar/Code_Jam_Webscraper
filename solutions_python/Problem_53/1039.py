import sys

def main():
	infile = open(sys.argv[1], "r")
	outfile = open("out.txt", "w")
	T = int(infile.readline())
	for i in range(1,T+1):
		# N snappers, K snaps
		(N,K) = infile.readline().split()
		N = int(N)
		K = int(K)
		snaps =  K % (2**N)	# RESETS SNAPS TO ZERO

		
		if snaps < 2**N - 1:
			bulb = "OFF"	# dont do tests, it is off
		elif snaps == 2**N - 1:
			bulb = "ON"

		outfile.write("Case #%d: %s\n" % (i, bulb))
if __name__ == "__main__":
  main()
