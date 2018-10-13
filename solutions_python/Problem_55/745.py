#!/usr/bin/python



def get(index, array):
#	return array[(index) % len(array)]
	return array[(index) % len(array)]


if __name__ == '__main__':
	import sys
	fname = sys.argv[1]
	f = open(fname, 'r')
	T = int(f.readline()) # The number of test cases

	for t in range(T):
		R, k, N = f.readline().split()
		R = int(R) # R = max runs 
		k = int(k) # k = capacity
		N = int(N) # N = array size
		array = map(int,f.readline().split())
	
		profit = 0
		index = 0
		for r in range(R):
			people_count = N # You cant have more than N people per ride
			temp = 0		# The size of this ride
			while True:
				if temp + get(index, array) <= k and people_count > 0:
					people_count -= 1
					profit += get(index, array)
					temp += get(index, array)
					if index+1 == N:
						index = 0
					else:
						index +=1
				else:
					break
		print 'Case #%d: %d' % (t+1, profit)
		profit = 0




