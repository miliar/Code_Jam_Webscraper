import fractions


def is_power2(num, count):
	if num == 1:
		return count
	elif (num%2==0):
		return is_power2(num/2,count+1)
	else:
		return -1

def smallerPowerN(num):
	power = 1
	count = 0
	if num == 1:
		return 0
	while num > power:
		 power *= 2
		 count += 1	
	return (count - 1)

input_file = "a.in"
infile = open(input_file)

lines = infile.readlines();
t = int( lines[0] )
lines = lines[1:]
for i in range(t):
	print "Case #" + str(i+1) + ": ",
	pq = lines[( i ) ].rstrip();
	p = int(pq[:pq.find('/')])
	q = int(pq[pq.find('/')+1:])
	g = fractions.gcd(p,q);
	p = p/g
	q = q/g
	val = is_power2(q,0)
	if ( val == -1):
		print "impossible"
	else:
		print val-smallerPowerN(p)
