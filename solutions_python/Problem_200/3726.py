
def get_ans(num):
	n = [ n for n in num]
	n = map(int, n)

	cnt = None

	for i in range(1,len(n)):
		if n[i] < n[i-1] :
			cnt = i-1
			break

	if cnt == None :
		return num

	cnt = None
	for i in range(1,len(n)):
		if n[i] <= n[i-1] :
			cnt = i-1
			break	
	
	l = []

	for i in range(len(n)):
		if i < cnt:
			l.append(n[i])
		elif i == cnt:
			l.append(n[i]-1)
		else:
			l.append(9)

	l = map(str,l)
	l = "".join(l)
	l = int(l)


	return l

fname = "input.txt"
fname = "B-small-attempt0.in"

f = open(fname,"r")

lines = f.readlines()

total = int(lines[0])
for i in range(total):
	s = lines[i+1].split("\n")[0]

	ans = get_ans(s)

	ans = "Case #"+str(i+1)+": "+ str(ans)
	print ans
