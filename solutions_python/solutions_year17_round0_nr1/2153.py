from sys import stdin



if __name__ == '__main__':
	n = int(stdin.readline())
	for i in range(n):
		line, pkk = stdin.readline().split()
		ipkk = int(pkk)
		lline = list(line)
		lenline = len(line)
		cutpoint = lenline - ipkk
		cc = 0

		for ii in range(cutpoint+1):
			if lline[ii] == '-':
				cc += 1
				for k in range(ipkk):
					ip = ii + k
					if lline[ip] == '+':
						lline[ip] = '-'
					else:
						lline[ip] = '+'

		res = True
		for ii in range(cutpoint,lenline):
			if(lline[ii] == '-'):
				res = False
				break
		if res == False:
			cc = 'IMPOSSIBLE'
		print("Case #{}: {}".format(i+1, cc))
