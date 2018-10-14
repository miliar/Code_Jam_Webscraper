import sys,math

cases = int(raw_input())
rows = []

for i in range(cases):
	wooo = raw_input().split(' ')
	what = wooo[0]
	ssss = wooo[1]

	a = 0
	s = []
	cum = 0
	sc = []

	for j in range(len(ssss)):
		s.append(int(ssss[j]))
		#sc.append(0)
		#for k in range(j+1):
		#	sc[j] += s[k]

		#print sc

		if j > 0 and j-(cum + a) > 0:
			a += j-(cum + a)

		cum += s[j]
	print ("Case #" + str(i+1) + ": " + str(a))


