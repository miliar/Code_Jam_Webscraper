import sys, math

def getInfo():
	file = open(sys.argv[1]);
	a = file.read().split("\n");
	n = int(a[0])
	a = a[1:]
	
	cases = []
	for i in range(n):
		b = a[i].split(" ");
		case = []
		for j in b:
			case.append(int(j))
		cases.append(case)
		
	return cases
	
def checkPal(num):
	n = str(num)
	i = 0;
	while(i < int(0.5*len(n))):
		if not (n[i] == n[len(n)-1-i]):
			return False
		i += 1;
	return True

	
def solveCase(case):
	count = 0;
	for i in range(case[0], case[1]+1):
		sqt = math.sqrt(i)
		if  not(sqt == int(sqt)): continue;
		if (checkPal(i) and checkPal(int(sqt))):
			 count += 1;
	return count;
	
def solveAll(cases, file):
	for i in range(len(cases)):
		file.write("Case #"+str(i+1)+": "+str(solveCase(cases[i]))+"\n")

if __name__ == "__main__":
	cases = getInfo()
	file = open(sys.argv[1]+".out", 'w')
	solveAll(cases, file)