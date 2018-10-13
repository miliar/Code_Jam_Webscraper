import time
input1 = []
digs = []


def verify(digs):
	tidy = 0;
	for n in xrange(len(digs)-1):
		if digs[n]>=digs[n+1]:
			#print "{} > {}".format(digs[n], digs[n+1])
			continue
		else :
			tidy += 1
	#print tidy
	if tidy == 0:
		#print digs
		return True
	else:
		return False

def readinput():
	filein = open("B-small-attempt0.in","r0")	
	size = int(filein.readline())
	print size
	content = filein.readlines()
	for x in content:
		input1.append(int(x.strip('/n')))
	print input1

def printdigit(digs):
	digitset = 0
	count = 0
	for x in digs:
		digitset += x*(10**count)
		count +=1
	return digitset

fileop = open("tidynumsop.out", "w+")
readinput()
count = 0
for number in input1:
	count += 1
	x = number
	start = time.time()
	while x > 0:
		#print x
		num = x
		digs = []
		while num > 0:
			dig = num % 10
			num = num/10
			digs.append(dig)
		if verify(digs)	:
			print("tidy number found --> {}".format(digs))
			fileop.writelines("Case #{}: {}\n".format(count, printdigit(digs)))
			print ("Case #{}: {}\n".format(count, printdigit(digs)))
			print (time.time() - start)
			
			break
		x -=1
