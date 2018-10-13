
from math import sqrt,floor,ceil
f = open('C-small-attempt0.in','r')
p = f.readlines()[1:]
f.close()

def palindrome(num):
	if str(num) == str(num)[::-1]:
		return True
	return False
c = 0
final_output = ""
for a in p:
	count = 0
	#find sqare roots to iterate through
	a = a.split()
	if len(a) < 1:
		break
	m,M = int(ceil(sqrt(int(a[0])))),int(floor(sqrt(int(a[1]))))+1
	for x in xrange(m,M):
		if palindrome(x) and palindrome(x**2):
			count += 1
	c+=1
	final_output += "Case #" + str(c) + ": " + str(count) + "\n"
f = open('output.txt','w')
f.write(final_output)
f.close()