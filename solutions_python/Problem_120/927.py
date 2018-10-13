import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
import itertools
import math
from random import random

def readstr(f): return f.readline()[:-1]
def readfloat(f): return float(readstr(f))
def readint(f): return int(readstr(f))
def readstrs(f): return readstr(f).split(' ')
def readints(f): return map(int, readstrs(f))
def readfloats(f): return map(float, readstrs(f))

def main():
	fn = raw_input('File name: ')
	f = open(fn)
	o = open('output.txt','w')
	no_cases = readint(f)
	for x in xrange(no_cases):
		para1 = readints(f)
		result = solver(para1[0],para1[1])
		o.write("Case #"+str(x+1) + ": " + result + '\n')
		logging.debug(str(x+1)+ "/"+ str(no_cases) +"Done")
	f.close()
	o.close()



def solver(r,t):
	logging.debug("r " + str(r) + " t "+ str(t))
	b = 2 * r - 1
	d = b * b + 8 * t
	logging.debug("d " + str(d))
	rt = math.sqrt(d)
	logging.debug("rt " + str(rt))
	x = (rt - b ) / 4
	x2 = (-rt - b) / 4
	logging.debug("x " + str(x))
	logging.debug("x2 " + str(x2))
	a = math.floor(x)
	logging.debug("a " + str(a))
	return str(int(a))
	# counter = 0
	# while t > 0:
	# 	t = t - (2 * r + 1) - 4 * counter
	# 	counter = counter + 1
	# return str(counter)


main()