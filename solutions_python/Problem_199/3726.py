import math
import sys
sys.setrecursionlimit(1500)


INF = 99999999999999

def check(string, length):
	if len(string) == length:
		if string == '+'*length:
			return 0
		elif string == '-'*length:
			return 1
		else:
			return INF
	else:
		if string[0] == '+':
			return check(string[1:], length)
		else:
			temp = list(string) 
			for i in range(1, length):
				if string[i] == '+':
					temp[i] = '-'
				else:
					temp[i] = '+'
			return check(''.join(temp[1:]), length) + 1


f = open('s.txt')
T = int(f.readline())
for t in range(T):
    sys.stdout.write('Case #' + str(t+1) + ': ')
    temp = f.readline().split()
    K = int(temp[-1])
    temp = temp[0:-1]
    temp = temp[0]
    out = check(temp, K)
    if out >= INF:
    	print("IMPOSSIBLE")
    else:
    	print(str(out))
    