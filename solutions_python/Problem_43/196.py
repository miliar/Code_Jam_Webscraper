from itertools import *

def unique_everseen(iterable, key=None):
	"List unique elements, preserving order. Remember all elements ever seen."
	# unique_everseen('AAAABBBCCDAABBB') --> A B C D
	# unique_everseen('ABBCcAD', str.lower) --> A B C D
	seen = set()
	seen_add = seen.add
	l = list()
	if key is None:
		for element in iterable:
			if element not in seen:
				seen_add(element)
				l.append(element)
				#yield element
	else:
		for element in iterable:
			print element
			k = key(element)
			if k not in seen:
				seen_add(k)
				l.append(element)
				#yield element
	return l
	
def translate(num, al, be):
	val1 = {}
	i = 0
	for c in al:
		val1[c] = i
		i += 1

	inum = 0
	mul = 1
	lnum = list(num)
	lnum.reverse()
	for c in lnum:
		inum += mul * val1[c]
		mul *= len(al)
		
	res = ''
	while inum > 0:
		i = inum % len(be)
		c = be[i]
		res = c + res
		inum /= len(be)
		
	return res

def read(f):
	return f.readline().replace("\n","")
	
f = open("a-in.txt")
cases = int(read(f))
out = open("a-out.txt", "w")
for c in xrange(cases):
	line = read(f)
	
	chars = unique_everseen(list(line))
	if len(chars) == 1:
		chars.insert(0, "0")
	else:
		k = chars.pop(1)
		chars.insert(0, k)
	
	min = None
	win_comb = None
	#print "Line: %s" % line
	
	min = int(translate(line, chars, '0123456789'))
	
	if min is None:
		min = 1
	#print min, win_comb
	out.write("Case #%d: %s\n" % (c+1, min))
out.close()
f.close()