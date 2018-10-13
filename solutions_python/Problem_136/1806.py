def get_int(s):
	return int(s[:(len(s)-1)])
	
def get_list_float(s):
	s = s[:len(s)-2]
	s = s.split(' ')
	result = []
	c = float(s[0])
	f = float(s[1])
	x = float(s[2])
	return c, f, x

def produce(c,f,x,rate):
	min = x/rate
	i = 1
	prev = 0
	while (True):
		prev += c/rate
		next = prev + x/(rate+f)
		rate += f
		if min < next:
			return min
		else:
			min = next
	
def process_file(filename):
	fin = open(filename,'r')
	n = get_int(fin.readline())
	for i in range(0,n):
		c, f, x = get_list_float(fin.readline())
		rate = 2.0
		ans = produce(c,f,x,rate)
		print 'Case #'+str(i+1)+':', ans
	return 0
	
if __name__ == '__main__':
	import sys
	if len(sys.argv) != 2:
		sys.stderr.write("USAGE: %s <coll-file>\n" % sys.argv[0])
		ys.exit()	
	l = process_file(sys.argv[1])