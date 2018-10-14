import sys
import math

outfile = open("output.txt","w")


def geti():							# get some integer
	return int(sys.stdin.readline())

def getis():						# get integer array
	return [int(i) for i in sys.stdin.readline().split()]
	
def pcase(case, output, fl = 0):	# print case
	ans = "Case #" + str(case) + ": " + str(output) + "\n"
	print(ans,end="")
	if fl:
		fl.write(ans)
	

def ispalin(n):
	s = str(n)
	if s[::-1] == s:	return 1
	return 0

	
cases = geti()
print("Cases: " + str(cases))

for case in range(1, cases + 1):
	A,B = getis()
	
	cnt = 0
	for i in range(A,B+1):
		if ispalin(i):
			sq = math.sqrt(i)
			if sq % 1 == 0 and ispalin(int(sq)) == 1:
					cnt += 1
				
	pcase(case, cnt, outfile)