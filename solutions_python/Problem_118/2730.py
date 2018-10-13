from math import sqrt,floor,ceil

N = input()

def is_palindrom(str):
	i = 0
	while i<len(str)/2 and str[i] == str[(-1*i)-1]:
		i+=1
	if(i == len(str)/2): return True
	return False

for x in xrange(1,N+1):
	line = raw_input()
	line = line.split()
	bot = ceil(sqrt(float(line[0])))
	top = floor(sqrt(float(line[1])))
	c = 0
	while bot<=top:
		if(is_palindrom("%.0f" % bot)):
			square = bot*bot
			if(is_palindrom("%.0f" % square)):
				c+=1
		bot+=1
	print "Case #%d: %d" % (x,c)


