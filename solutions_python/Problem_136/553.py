import sys,math

fi = open('cookie.in.l', 'r')

T = int(fi.readline().rstrip('\n'))

for i in range(1, T+1):
		params = fi.readline().rstrip('\n').split(' ')
		C = float(params[0])
		F = float(params[1])
		X = float(params[2])
		n = math.floor((F*X - 2*C)/(C*F)-1)

		if n < 0:
				n = -1
		result = 0.0
		for k in range(int(n)+1):
				result += C / (2 + k*F)
		result += X / (2 + (n+1)*F)
		print "Case #%d: %.7f" % (i,result)
