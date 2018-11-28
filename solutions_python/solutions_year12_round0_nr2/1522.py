f = open("C:/Documents and Settings/Snuderl/Desktop/file.txt")
input = f.read()


def greatestDivisor(a, max=10):
	for i in range(max,0,-1):
		if( (a/i) > 0):
			return i



def triplet(n):
	n = int(n)
	a = n/3
	ostanek = n%3
	if(ostanek==0):
		return (a,a,a)
	elif(ostanek==1): return (a+1,a,a)
	elif(ostanek==2): return(a+1,a+1,a)
	else:
		raise Exception("Ostnanek ni med 0 in 2")



def isSuprisingEnough(t, p):
	if(max(t)==(p-1) and max(t)!=0):
		m = max(t)
		if(len([x for x in t if x==m]) >= 2):
			return True
	return False

def procesLine(line):
	correct = 0
	posibleSupr = 0
	line = line.split(" ")
	googlers = line[0]
	surprising = int(line[1])
	p = int(line[2])
	line = line[3:len(line)]
	for n in line:
		t = triplet(n)
		if(max(t)>=p):
			correct=correct+1
		elif(isSuprisingEnough(t,p)):
			posibleSupr=posibleSupr+1
	correct += min(posibleSupr, surprising)
	return correct


lines = input.split("\n")
numCases = lines[0]
lines = lines[1:len(lines)]

r = open("C:/Documents and Settings/Snuderl/Desktop/result.txt", "r+")
for i,l in enumerate(lines):
	r.write("Case #"+str(i+1)+": "+str(procesLine(l))+"\n")

