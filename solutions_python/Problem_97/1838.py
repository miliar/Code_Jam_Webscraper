seen = []
def isRec(num, bound1, bound2):
	global seen
	s = str(num)
	origS = s[:]
	lst = []
	for i in range(len(s)):
		s = s[1:] + s[0]
		if s == origS:
			if lst:
				return len(lst)
			else: return 0
		elif s not in lst and bound1 <= int(s) <= bound2 and (s, origS) not in seen and (origS, s) not in seen:
			lst.append(s)
	return len(lst)

fin = open('C-small-attempt0.in', 'r')
fout = open('3lines.out', 'w')
N = int(fin.readline())
for i in range(N):
	s = fin.readline().split()
	sum = 0
	for j in range(int(s[0]), int(s[1]) + 1):
		sum += isRec(j, int(s[0]), int(s[1]))
	fout.write('Case #' + str(i + 1) + ': ' + str(sum // 2) + '\n')



