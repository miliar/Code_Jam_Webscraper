def allConsonants(s):
	vowels = ('a','e','i','o','u')
	for c in s:
		if c in vowels:
			return False
	return True

def nvalue(name, n):
	l = len(name)
	v = 0
	last = -1
	for i in range(l + 1 - n):
		s = name[i:i+n]
		if allConsonants(s) :
			v += (i - last) * (l + 1 - i - n)
			last = i
		#print s, v
	return v

# starts here
import sys
l = sys.stdin.readline()
count = int(l)

for i in range(count):
	data = sys.stdin.readline().split()
	name = data[0]
	n = int(data[1])
	v = nvalue(name, n)

	print "Case #" + str(i+1) + ": " + str(v)
    
