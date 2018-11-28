import math

#inp = file("test.in")
#inp = file("B-small-attempt2.in")
inp = file("B-large.in")
#result = file("test.out", "w")
#result = file("B-small-attempt2.out", "w")
result = file("B-large.out", "w")

def decodeMinutes(s):
	h = int(s[0:2])
	m = int(s[3:5])
	return m + h * 60

def calc(turnaround, atob, btoa):
	trainsA = 0
	trainsB = 0
	while len(atob) > 0 or len(btoa) > 0:
		readyTime = 0
		if len(btoa) == 0 or (len(atob) > 0 and atob[0][0] <= btoa[0][0]):
			station = 0
			trainsA += 1
			print "train from A", trainsA
		else:
			station = 1
			trainsB += 1
			print "train from B", trainsB
			
		found = True
		while found:
			found = False
			if station == 0:
				i = 0
				while i < len(atob) and atob[i][0] < readyTime:
					i += 1
					
				if i < len(atob):
					print "arrive at B at" + str(atob[i][1]), i
					readyTime = atob[i][1] + turnaround
					atob = atob[:i] + atob[i + 1:]
					station = 1
					found = True
			else:			
				i = 0
				while i < len(btoa) and btoa[i][0] < readyTime:
					i += 1
					
				if i < len(btoa):
					print "arrive at A at" + str(btoa[i][1]), i
					readyTime = btoa[i][1] + turnaround
					btoa = btoa[:i] + btoa[i + 1:]
					station = 0
					found = True
	
	return trainsA, trainsB


def compare(a, b):
	return a[0] - b[0]

cases = int(inp.readline())
for case in range(cases):
	print "Doing case " + str(case)
	turnaround = int(inp.readline())
	line = inp.readline()
	line = line.strip()
	values = line.split()

	atobCount = int(values[0])
	btoaCount = int(values[1])

	atob = []
	btoa = []
		
	for i in range(atobCount):
		line = inp.readline()
		line = line.strip()
		values = line.split()
		
		atob.append((decodeMinutes(values[0]), decodeMinutes(values[1])))

	for i in range(btoaCount):
		line = inp.readline()
		line = line.strip()
		values = line.split()
		
		btoa.append((decodeMinutes(values[0]), decodeMinutes(values[1])))
	
	atob = sorted(atob, compare)
	btoa = sorted(btoa, compare)
	
	
	print turnaround, atob, btoa
	r = calc(turnaround, atob, btoa)
	result.write("Case #" + str(case + 1) + ": " + str(r[0]) + " " + str(r[1]) + "\n")