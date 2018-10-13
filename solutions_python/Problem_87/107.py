import sys,copy

B = []
E = []
w = []
dicF = {}
lf = []

n = 0
l = 0
N = 0
for line in sys.stdin:
	if n == 0:
		n = 1
		continue
	word = line.split()
	if l == 0:
		l = 1
		X = int(word[0])
		S = int(word[1])
		R = int(word[2])
		t = int(word[3])
		N = int(word[4])
		B = []
		E = []
		w = []
		dicF = {}
		lf = []
		continue
	elif l < N:
		B += [int(word[0])]
		E += [int(word[1])]
		w += [int(word[2])]
		l += 1
		continue
	else:
		l = 0
		B += [int(word[0])]
		E += [int(word[1])]
		w += [int(word[2])]
		ds = 0
		for i in range(N):
			F = w[i] + S
			if dicF.has_key(F):
				dicF[F] += (E[i] - B[i])
			else:
				dicF[F] = E[i] - B[i]
			ds += (E[i] - B[i])
		dicF[S] = X - ds
		
		for skey in dicF.keys():
			lf += [skey]
		lf.sort()
		tt = t
		tim = 0.0
		for i in range(len(lf)):
			tmpT = float(dicF[lf[i]])/float(lf[i] + R - S)
			
			
			if(tt - tmpT >= 0):
				tim += tmpT
				tt -= tmpT
			elif tt > 0:
				tmpD = float(dicF[lf[i]]) - float(tt) * float(lf[i] + R - S)
				tim += (tt + tmpD/float(lf[i]))
				tt = 0
			else:
				tim += (float(dicF[lf[i]])/float(lf[i]))
		print "Case #" + str(n) + ": " + str(tim)
		n += 1
