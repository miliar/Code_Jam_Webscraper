R_i=lambda x:map(int, x.strip().split(' '))

inp = open("A-small-attempt0.in", "r")
def R():
	line = inp.readline()
	return R_i(line) 

f = open("output.txt", "w")

def get_matrix():
	target, = R()
	i = 0
	ret = []
	while i < 4:
		row = R()
		if i + 1== target:
			ret = row
		i += 1
	return ret

T,=R()

cnt = 0
while cnt < T:
	print "??", cnt
	cnt += 1
	row_pre = get_matrix()
	row_last = get_matrix()

	print "??", row_pre, row_last
	ret = list(set(row_pre).intersection(set(row_last)))
	f.write("Case #%d: " % cnt)
	if len(ret) == 0:
		f.write("Volunteer cheated!\n")
	elif len(ret) > 1:
		f.write("Bad magician!\n")
	else:
		f.write("%d\n" % ret[0])
