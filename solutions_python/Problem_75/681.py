import sys

fi = open("input.txt", "r")
fo = open("output.txt", "w")

c = int(fi.readline().strip());
for tc in range(1, c + 1):
	tmp = list(map(str, fi.readline().strip().split(" ")))
	
	nborn = int(tmp[0])
	born = []
	for i in range(1, nborn + 1):
		born.append(tmp[i])

	nkill = int(tmp[2 + nborn - 1])
	kill = []
	for i in range(2 + nborn - 1 + 1, 2 + nborn - 1 + nkill + 1):
		kill.append(tmp[i])

	n = int(tmp[2 + nborn - 1 + nkill + 1])
	seq = tmp[2 + nborn - 1 + nkill + 1 + 1]

	s = []
	k = 0
	s.append(seq[k])
	k = 1
	while k < n:
		s.append(seq[k])
		if len(s) > 1:
			l2 = s[len(s) - 1] + s[len(s) - 2]
			for i in range(0, nborn):
				if l2 == (born[i][0] + born[i][1]) or l2 == (born[i][1] + born[i][0]):
					s[len(s) - 2] = born[i][2]
					s = s[:-1]
			for i in range(0, nkill):
				ok1 = False
				ok2 = False
				for j in range(0, len(s)):
					if s[j] == kill[i][0]:
						ok1 = True
					if s[j] == kill[i][1]:
						ok2 = True
				if ok1 and ok2:
					s = []
		k = k + 1

	ans = str(s)
						
	fo.write("Case #{0}: {1}\n".format(tc, str(ans)))
	
fi.close()
fo.close()