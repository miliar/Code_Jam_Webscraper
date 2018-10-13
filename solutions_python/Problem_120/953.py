import math
import decimal
file_handle = open('input.txt', 'r')
f = open('output.txt', 'w')
lines_list = file_handle.readlines()
T = int(lines_list[0])
my_data = [[int(val) for val in line.split()] for line in lines_list[1:]]
decimal.getcontext().prec = 100
for Z in range(0, T):
	r = decimal.Decimal(my_data[Z][0])
	t = decimal.Decimal(my_data[Z][1])
	x = decimal.Decimal(1.0/4)*(decimal.Decimal(1)-decimal.Decimal(2*r)+(4*r*r-4*r+8*t+1).sqrt())
	f.write("Case #"+str(Z+1)+": "+str(int(math.floor(x)))+"\n")
