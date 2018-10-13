import math

f = open('C-small-attempt2.in','r')
o = open('output.txt','w')

n = f.readline()
n = int(n)

for case in range(1,n+1):

	a,b = f.readline().split()
	a = int(a)
	b = int(b)
	
	first = 0
	x = a
	while ( x <= b):
		if (math.sqrt(x).is_integer()):
			first = x
			break
		x += 1

	count = 0
	
	if ( first == 0):
		o.write("Case #" + str(case) + ": " + str(count) + "\n")
		continue
	
	if (str(first) == str(first)[::-1]):
		if (  str(int(math.sqrt(first))) == str(int(math.sqrt(first)))[::-1]):
			count = 1

	diff = 2*math.sqrt(first) + 1
	

	while (first + diff <= b):
		if str(first+int(diff)) == str(first+int(diff))[::-1]:
			if (  str(int(math.sqrt(first+int(diff)))) == str(int(math.sqrt(first+int(diff))))[::-1]):
				count += 1
		first += int(diff)
		diff += 2

	o.write("Case #" + str(case) + ": " + str(count) + "\n")

f.close()
o.close()
