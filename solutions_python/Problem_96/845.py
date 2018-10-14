f = open('file.in', 'r')
data = f.readlines()
for i in range(1, len(data)):
	#data[i] = data[i][:-1]
	args = data[i].split()
	N = int(args[0]); S = int(args[1]); p = int(args[2])
	j = 3
	ans = 0
	while j < len(args):
		total = int(args[j])
		jdg = total / 3
		if jdg >= p or total % 3 != 0 and jdg + 1 >= p:
			ans += 1
		elif total % 3 == 2 and jdg + 2 == p and S:
			S -= 1; ans += 1
		elif total % 3 == 0 and total and jdg + 1 == p and S:
			S -= 1; ans += 1
		j += 1
	print "Case #" + str(i) + ": " + str(ans)
