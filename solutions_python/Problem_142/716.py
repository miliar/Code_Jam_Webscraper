from collections import *

inFile = open("input.txt", "r")

outFile = open("out.txt", "w")

T = int(inFile.readline())

for t in xrange(T):
	outFile.write("Case #" + str(t+1) + ": ")
	k = inFile.readline()
	n = int(k)
	sl = []
	cl = []
	for ss in xrange(n):
		sl.append(inFile.readline().rstrip())

	cl = [[] for i in xrange(n)]

	for i in xrange(n):
		k = sl[i][0][0]
		c = sl[i][0]
		ln = len(sl[i])
		cnt = 1
		cl[i].append(cnt)
		for j in xrange(1,ln):
			if c != sl[i][j]:
				k+= sl[i][j]
				c = sl[i][j]
				cnt = 1
				cl[i].append(cnt)
			else:
				cnt+=1
				cl[i][len(k)-1] = cnt

		sl[i] = k

	if all(s == sl[0] for s in sl):
		t = 0
		for i in xrange(len(sl[0])):
			f = []
			for j in xrange(n):
				f.append(cl[j][i])

			m_min = min(f)
			m_max = max(f)
			r_min = 1000
			for j in xrange(m_min,m_max+1):
				s = 0
				for ff in f:
					s += abs(ff - j)
				r_min = min(r_min,s)
			t += r_min
		outFile.write(str(t))
	else:
		print("Fegla Won")
		outFile.write("Fegla Won")

	print(sl)
	print(cl)



	outFile.write("\n")

