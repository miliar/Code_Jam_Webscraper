
fin = open("a_in.txt", "r")
fout = open("a_out.txt", "w")

datas = fin.readlines()

case = int(datas[0])
for c in range(0, case):
	d = datas[c + 1]
	line = d.split()
	t = int(line[0])
	ret = 0
	s_sum = 0
	for i in range(0, t):
		val = int(line[1][i])
		s_sum += val
		if s_sum < i + 1:
			ret += 1
			s_sum += 1
	print("Case #%d: %d" % (c + 1, ret), file = fout)
