import sys

def count(case,C,F,X):
	with open('B.out','a') as f:
		cookies = 2
		time = 0
		flag = True
		while C/cookies + X/(cookies+F) <= X/cookies:
			flag = False
			time += C/cookies
			cookies += F
		time += X/cookies
		f.write("Case #%d: %.7f\n" % (case, time))

with open(sys.argv[1]) as f:
	case = int(f.readline())
	for i in range(case):
		C,F,X = f.readline().split(' ')
		count(i+1,float(C),float(F),float(X))