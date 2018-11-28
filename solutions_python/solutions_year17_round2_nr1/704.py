import sys
import itertools

#filename = "test.in"
filename = None
#filename = "A-small-attempt1.in"


def solve(casenum, D,N,horses):
	#print casenum, D, N, horses
	times = [(D-offset)*1.0/speed for offset, speed in horses if offset < D]

	worst_time = max(times)
	#print times
	#print worst_time
	print "Case #%i: %.6f" % (casenum+1, D*1.0/worst_time )

def main():
	if filename:
		file = open(filename)
	else:
		file = sys.stdin


	T = int(file.readline().strip())
	for casenum in range(T):	
		D, N = map(int, file.readline().strip().split())
		horses = []
		for i in range(N):
			K, S = map(int, file.readline().strip().split())
			horses.append((K,S))
		solve(casenum, D,N,horses)
		

	if file is not sys.stdin:
	    file.close()



if __name__ == '__main__':
	main()
