from collections import *

file = open("input.txt", "r")

outFile = open("out.txt", "w")
T = int(file.readline())

for t in xrange(T):
	N = int(file.readline())
	
	a = [ float(weight) for weight in file.readline().split()]
	b = [ float(weight) for weight in file.readline().split()]

	win_honest = 0

	win_lie = 0

	a.sort()
	b.sort()

	cnt = defaultdict(bool)

	for el in a:
		is_win = True
		for j, elb in enumerate(b):
			if not cnt[j]:
				if elb > el:
					is_win = False
					cnt[j] = True
					break
		if is_win:
			win_honest+=1

	for el in a:
		if el < min(b):
			b.pop()
		else:
			win_lie+=1
			b.pop(0)

	outFile.write("Case #" + str(t+1) + ": " + str(win_lie) + " " + str(win_honest)+ "\n")
