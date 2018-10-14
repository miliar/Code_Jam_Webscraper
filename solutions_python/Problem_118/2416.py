import math

def palin(a):
	if len(str(a))%2 == 0:
		z = str(a)[:len(str(a))/2]
		x = str(a)[len(str(a))/2:][::-1]
	else:
		z = str(a)[:len(str(a))/2]
		x = str(a)[len(str(a))/2+1:][::-1]
	if z == x:
		return 1
	else:
		return 0

f = open('c-small', 'r')
out = open('c-small-output.txt', 'w')
total = f.readline()
for tt in range(int(total)):
	count = 0
	fst = f.readline().split(" ")
	#print int(fst[0])
	#print int(fst[1])
	#print range(int(math.ceil(math.sqrt(int(fst[0])))),int(math.sqrt(math.floor(int(fst[1]))))+1)
	for v in range(int(math.ceil(math.sqrt(int(fst[0])))),int(math.sqrt(math.floor(int(fst[1]))))+1):
		if palin(v):
			if palin(v*v):
				count = count + palin(v)
				#print "- " + str(v)
	out.write("Case #" + str(tt+1) + ": " + str(count) + "\n")