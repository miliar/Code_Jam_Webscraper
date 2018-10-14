import math
from decimal import *

PI = math.pi
TWO = Decimal(2)
ONE = Decimal(1)

def checker(r, t):
	R = Decimal(r)
	T = Decimal(t)
	luggage = R/2-ONE/4
	type(luggage)
	num_rings = Decimal.sqrt(T/TWO+luggage**TWO)-luggage
	check = TWO*R*num_rings+TWO*num_rings**TWO-num_rings
	#print r, t, num_rings, check
	while (check - T) > (1*10**-18):
		num_rings -= ONE
		check = TWO*R*num_rings+TWO*num_rings**TWO-num_rings
	return int(math.floor(num_rings))
	

input_file = open('small_input', 'r')
output_file = open('small_output', 'w')
#input_file = open('large_input', 'r')
#output_file = open('large_output', 'w')
num_cases = int(input_file.readline())
output = ''

for i in range(1, num_cases+1):
	r, t = input_file.readline().split()
	output += 'Case #{0}: {1}\n'.format(i, checker(r, t))	
#print output
output_file.write(output)

output_file.close()
input_file.close()