import sys

cases = sys.stdin.readline()
cases = int(cases)

data1 = [] 
data2 = []

def inputing():
	global row1
	global row2
	global data1
	global data2

	row1 = int(sys.stdin.readline())
	for i in range(4):
		x = sys.stdin.readline().strip()
		if row1  == i + 1:
			data1 = x
			data1 = map(lambda y:int(y), data1.split() )

	row2 = int(sys.stdin.readline())
	for i in range(4):
		x = sys.stdin.readline().strip()
		if row2  == i + 1:
			data2 = x
			data2 = map(lambda y:int(y), data2.split() )

	#print data1,data2

def work(idx):
	num = 0
	rowx = -1
	for i in range(4):
		for j in range(4):
			if data1[i] == data2[j]:
				rowx = data1[i]
				num += 1
	if num > 1:
		print "Case #%d: %s!" % (idx, "Bad magician");
	if 0 == num:
		print "Case #%d: %s!" % (idx, "Volunteer cheated");
	if 1 == num:
		print "Case #%d: %d" % (idx, rowx);


for i in range(cases):
	inputing()
	work(i+1)


