import sys

pattern = "Case #{0}: {1}"
cannot = "Fegla Won"


		
def reduceString(s):
	t = []
	f = []
	temp = 0
	for i in s:
		if not f:
			f.append(i)
		elif i != f[-1]:
			f.append(i)
			t.append(temp)
			temp = 0
		else:
			temp+=1
	t.append(temp)
	return "".join(f),t

def score(a,b):
	return sum([abs(i-j) for i,j in zip(a,b)])

def getData(n,f):
	t = []
	s = ""
	zero = 0
	for i in xrange(n):
		stemp = ""
		if not t:
			s,temp = reduceString(f.readline().rstrip("\n"))
			zero += sum(temp)
			sc = 0
		else:
			stemp,temp = reduceString(f.readline().rstrip("\n"))
			if stemp != s:
				return -1
			else:
				zero += sum(temp)
				sc = 0
				for ind, elt in enumerate(t):
					sctemp = score(temp,elt[0])
					t[ind][1] += sctemp
					sc += sctemp
		t.append([temp,sc])
	m =  min([x[1] for x in t]+[zero])
	return m

if __name__=="__main__":
	with open(sys.argv[1]) as f:
		ntests = int(f.readline())
		for i in xrange(1,ntests+1):
			n = int(f.readline())
			result = getData(n,f)
			if result < 0:
				print pattern.format(i,cannot)
			else:
				print pattern.format(i,result)

