inputN = "A-small-attempt0.in"
outputN = "output.txt"

def readInp(fileName):
	with open(fileName,'r') as inp:
		T = inp.readline()
		for i in range(int(T)):
			r1 = inp.readline()
			cards1 = []
			for _ in range(4):
				s = inp.readline()
				cards1.append(s.split())
			r2 = inp.readline()
			cards2 = []
			for _ in range(4):
				s = inp.readline()
				cards2.append(s.split())
			check(i,r1,r2,cards1,cards2)

def check(i,r1,r2,cards1,cards2):
	a = [x for x in cards1[int(r1)-1] for y in cards2[int(r2)-1] if x==y]
	if len(a)==0:
		ans = "Volunteer cheated!"
	elif len(a)>1:
		ans = "Bad magician!"
	else:
		ans = a[0]
	writeOut(outputN,i,ans)

def writeOut(fileName,i,ans):
	if i==0:
		with open(fileName,'w') as out:
			out.write("Case #{0}: {1}\n".format(i+1,ans))
	else:
		with open(fileName,'a') as out:
			out.write("Case #{0}: {1}\n".format(i+1,ans))

readInp(inputN)