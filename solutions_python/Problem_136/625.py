#gc COOKIE Clicker
import string
from math import *

if __name__ == "__main__":
	input = open('B-large.in')
	output = open('cookie_output.txt','w')
	
	n_test = int(input.readline().replace('\n',''))
	
	for n in xrange(1,n_test+1):
		set = input.readline().replace('\n','').split(' ')
		set = [float(k) for k in set]
		C, F, X = set
		
		cookie_rate = float(2)
		cookie_time = float(0)
		cookies = float(0)
		finished = False
		
		while not finished:
			curr_time = (X-cookies)/cookie_rate
			next_time = float(0)
			if cookies == C:
				next_time = X/(cookie_rate+F)
				if next_time < curr_time:
					cookie_rate += F
					cookie_time += C/cookie_rate
					cookies = C
				else:
					cookie_time += curr_time
					cookies = X
					finished = True
			else:
				if X-cookies <= C:
					cookies = X
					cookie_time += curr_time
					finished = True
				else:
					cookie_time += C/cookie_rate
					cookies = C
			
		output.write("Case #%d: %.9f\n" % (n, cookie_time))
	
	input.close()
	output.close()