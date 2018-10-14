f = open('B-small-attempt0.in', 'r')
fout = open('B-out.txt', 'w')

t = int(f.readline().strip())
rybdic = ["R", "Y", "B"]

def getCol(dic, maxnum, first):
	if first in dic.keys():
		if dic[first] == maxnum:
			return first
	for col, num in dic.items():
		if num == maxnum:
			return col

for i in range(t):
	fout.write("Case #%d: " %(i+1))
	print("Case #%d: " %(i+1))
	unis = f.readline().strip().split()
	total = int(unis[0])
	r = int(unis[1])
	y = int(unis[3])
	b = int(unis[5])
	ryb = [r,y,b]
	dic = {"R":r, "Y":y, "B":b}

	if (r>total/2.0 or y>total/2.0 or b>total/2.0):
		fout.write("IMPOSSIBLE\n")
	else:
		outp = ""
		maxnum = max(dic.values())
		maxcol = getCol(dic, maxnum, False)
		outp+=maxcol
		tup = (maxcol, maxnum-1)
		first = maxcol

		for u in range(total-1):
			del dic[tup[0]]
			maxnum = max(dic.values())
			maxcol = getCol(dic, maxnum, first)
			outp+=maxcol
			dic[tup[0]] = tup[1]
			tup = (maxcol, maxnum-1)
		print outp
		fout.write(outp+"\n")