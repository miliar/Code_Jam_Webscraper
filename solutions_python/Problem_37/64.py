import sys

jmd = set()

def isHappy(num, base):
	#print num
	#print jmd
	
	if num == 1:
		return True
		
	if num in jmd:
		return False
		
	jmd.add(num)
	
	sum = 0
	
	while num != 0:
		last = num % base
		sum += last * last
		num /= base
		
	return isHappy(sum, base)

input = sys.stdin

for i in range(0, int(input.readline())):
	f = [int(x) for x in input.readline().split()]
	for num in range(2, 100000):
		ok = True
		for factors in f:
			#print num, factors
			jmd.clear()
			if isHappy(num, factors) != True:
				ok = False
				break
		if ok:
			print "Case #%d: %d" % (i+1, num)
			break
	