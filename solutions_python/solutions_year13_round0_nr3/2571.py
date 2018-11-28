import math

def solve(path):
	f = open(path)
	count = int(f.readline())
	for i in range(count):
		case = f.readline().split()
		print "Case #"+str(i+1)+":", check(int(case[0]),int(case[1]))
		
def check(a,b):
	res = 0
	for n in range(a,b+1):
		if len(str(n)) == 1:
			if math.sqrt(n).is_integer():
				res +=1
		else:
			if str(n) == str(n)[::-1]:
				if math.sqrt(n).is_integer():
					r = str(int(math.sqrt(n)))
					if (len(r) == 1) or (r == r[::-1]):
						res +=1
	return res
	
solve("C-small-attempt0.in")