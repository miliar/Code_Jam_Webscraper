import sys
import simplejson

def toggle(a, k):
	for i in range(0,k):
		if a[i] == 0:
			a[i] = 1
		elif a[i] == 1:
			a[i] = 0




filePath = sys.argv[1]
outputFile = sys.argv[2]
f = open(filePath,'r')
fileContents = f.read()
lines = fileContents.split('\n')
of = open(outputFile,'w')

T = int(lines[0])



for u in range(1,T+1):
	index = 0
	sum = 0
	R = int(lines[2*u - 1].split(" ")[0])
	K = int(lines[2*u - 1].split(" ")[1])
	N = int(lines[2*u - 1].split(" ")[2])
	print "R: " + str(R) + ", K:" + str(K) + ", N:" +  str(N)
	a = []
	for i in range(0,N):
		print lines[2*u].split(" ")[i]	
		a.append(int(lines[2*u].split(" ")[i]))
	for r in range(1,R+1):
		print "run #:" + str(r)
		onBoard = 0
		for i in range(0,N):
			print "index:" + str(index)
			onBoard += a[index]
			print "onBoard:" + str(onBoard)
			if onBoard > K:
				onBoard = onBoard - a[index]
				print "turn"
				print "onBoard:" + str(onBoard)
				print "index:" + str(index)
				print "turn"

				break
			else:
				index += 1
			if index >= N:
				index = 0
				print "turn"
				print "onBoard:" + str(onBoard)
				print "index:" + str(index)
				print "turn"
		sum += onBoard
		print sum

	of.write("Case #" + str(u) + ": " + str(sum) + '\n')



