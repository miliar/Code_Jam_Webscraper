fin = open("b.in")
fout = open("b.out", "w")
nt = int(fin.readline())

def index_break(tofix):
	for i in range(len(tofix) - 1):
		if tofix[i] > tofix[i + 1]:
			return i
	return -1

def transform(tofix, tail):
	i = index_break(tofix)
	if i == -1:
		return tofix + tail
	num = int(tofix[:i+1])
	num -= 1
	pref = str(num)
	tail = "9" * (len(tofix) - i - 1) + tail
	return transform(pref, tail)


for tn in xrange(nt):
	fout.write("Case #" + str(tn + 1) + ": ")

	s = fin.readline().strip()
	res = transform(s, "")
	while res[0] == "0":
		res = res[1:]

	fout.write(res)
	fout.write("\n")
