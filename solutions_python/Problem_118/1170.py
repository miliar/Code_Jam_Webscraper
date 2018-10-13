import sys
import math

def pallindrom(s):
	for i in range(len(s)/2):
		if s[i]!=s[-1*i-1]:
			return False
	return True

assert pallindrom("1")
assert not pallindrom("12")
assert pallindrom("66")
assert not pallindrom("663")
assert pallindrom("363")
assert not pallindrom("4634")
assert pallindrom("4664")

inp = open(sys.argv[1],"r")
outp = open(sys.argv[2],"w")
case_count = int(inp.readline())
for case_num in range(1,case_count+1):
	AB = map(lambda s:int(s),inp.readline().strip().split())
	assert( len(AB)==2)
	A = AB[0]
	B = AB[1]
	count = 0
	for i in range(A,B+1):
		if pallindrom(str(i)):
			sqrt = math.sqrt(i)
			if int(sqrt)==sqrt:
				sqrt = int(sqrt)
				if pallindrom(str(sqrt)):
					count += 1
	outp.write("Case #%i: %i\n"%(case_num,count))