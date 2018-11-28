
def get_ans(ln):
	# print ln
	ln = ln.split(" ")
	num = int(ln[0])
	tc = int(ln[1])

	l = [num]
	cnt = 0

	while l != []:

		num = max(l)
		l.remove(num)

		if num % 2 == 0:
			n1 = num / 2
			n2 = num / 2 - 1
		else:
			n1 = n2 = num/2

		cnt += 1
		if cnt == tc:
			return "%d %d" % ( n1,n2)
		if n1 != 0:
			l.append(n1)
		if n2 != 0:
			l.append(n2)


fname = "ip3.txt"
fname = "C-small-1-attempt0.in"
fname = "C-small-1-attempt1.in"

f = open(fname,"r")

lines = f.readlines()

total = int(lines[0])
for i in range(total):
	s = lines[i+1].split("\n")[0]

	ans = get_ans(s)

	ans = "Case #"+str(i+1)+": "+ str(ans)
	print ans
