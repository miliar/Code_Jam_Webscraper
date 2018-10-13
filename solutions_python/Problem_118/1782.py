import math, code

fair_list = {}

def is_fair(i):
	if i in fair_list:
		return True
	if(i%1 != 0):
		return False
	i = int(i)
	string  = str(i)
	length = len(string)
	for i in range(length/2):
		if(string[i] != string[length-i-1]):
			return False
	fair_list[i] = 1
	return True

def is_square(i):
	return is_fair(math.sqrt(i))


counts = {}
counts[0] = 0
count = 0
upper = 1001
for i in xrange(1,upper):
	if i % 10000 == 0:
		print (i*100)/float(upper)
	if is_fair(i) and is_square(i):
		count+=1
	counts[i] = count


inp = open("fair.in")
num = int(inp.next().strip())

for i in range(num):
	string = inp.next().strip()
	sp_ind = string.find(" ")
	l = int(string[:sp_ind])
	u = int(string[sp_ind+1:])
	print ("Case #%d" % (i+1))+":",counts[u]-counts[l-1]