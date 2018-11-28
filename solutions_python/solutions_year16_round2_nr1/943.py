from sets import Set
import math
from collections import Counter
import copy

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

DP = [[-1 for x in range(101)] for y in range(101)]

def recur(n, k):
	if(DP[n][k] < 0):
		if(k == 1):
			DP[n][k] = 1
			return 1
		if(n==k):
			DP[n][k] = math.factorial(k)
			return DP[n][k]
		DP[n][k] = k*recur(n-1, k-1) + k*recur(n-1, k)
		return DP[n][k]
	else:
		return DP[n][k]

def main():

	N = raw_input()
	N = int(N)
	global DP


	for it in xrange(N):
		
		Lis = list(raw_input())
		s = Counter(Lis)

		#print s

		num_zer = s['Z']
		num_two = s['W']
		num_four = s['U']
		num_one = s['O'] - num_zer - num_two - num_four
		
		

		num_six = s['X']
		num_eight = s['G']
		
		
		num_sev = s['S'] - num_six

		num_three = s['H'] - num_eight
		
		num_five = s['V'] - num_sev 

		num_nume = s['I'] - num_eight - num_six - num_five


		#print ans
		#ans = ans % 1000000007
		li = []


		for i in xrange (num_zer):
			li.append('0') 

		for i in xrange (num_one):
			li.append('1') 

		for i in xrange (num_two):
			li.append('2') 

		for i in xrange (num_three):
			li.append('3') 

		for i in xrange (num_four):
			li.append('4') 

		for i in xrange (num_five):
			li.append('5') 

		for i in xrange (num_six):
			li.append('6') 

		for i in xrange (num_sev):
			li.append('7') 

		for i in xrange (num_eight):
			li.append('8') 

		for i in xrange (num_nume) :
			li.append('9') 

		st = ''.join(li)
		print 'Case #' + str(it+1) + ': ' + st 


if __name__ == '__main__':
	main()