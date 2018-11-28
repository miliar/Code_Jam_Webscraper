br = open("input.txt", "r")
out = open("output.txt", "w")

casenum = 0

def func():
	global casenum
	temp = br.readline()
	casenum = int(temp)
	for i in range(casenum):
		temp = br.readline()
		temp = temp.split()
		row = int(temp[0])
		col = int(temp[1])
		al = []
		for r in range(row):
			temp = []
			s1 = br.readline()
			s1 = s1.split()
			for c in range(col):
				temp.append(int(s1[c]))
			al.append(temp)
		print al

		while True:
			k = 0
			while k < len(al):
				if len(al[k]) == 0:
					del al[k]
					continue
				k += 1

			if len(al) == 0:
				break

			min1 = 100000
			minr = 0
			minc = 0
			for r in range(len(al)):
				for c in range(len(al[0])):
					if min1 > al[r][c]:
						minr = r
						minc = c
						min1 = al[r][c]

			numc = 0
			numr = 0
			rb = True
			cb = True
			for j in range(len(al[minr])):
				if al[minr][j] == min1:
					numr += 1

			if numr != len(al[minr]):
				rb = False

			for j in range(len(al)):
				if al[j][minc] == min1:
					numc += 1
			if numc != len(al):
				cb = False

			if cb == False and rb == False:
				print "Case #" + str(i + 1) + ": NO\n"
				out.write("Case #" + str(i + 1) + ": NO\n")
				break

			if cb:
				for j in range(len(al)):
					del al[j][minc]
				continue
			elif rb:
				del al[minr]
				continue

		if len(al) != 0 :
			continue
		print "Case #" + str(i + 1) + ": YES\n"
		out.write("Case #" + str(i + 1) + ": YES\n")



func()