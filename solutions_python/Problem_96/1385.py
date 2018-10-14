from sys import argv

script, rname, wname = argv

casefile = open(rname)

tc = int(casefile.readline())

ans = []

for i in range(0, tc):
	answer = 0
	case = map(int, casefile.readline().split(' '))
	n = case[0]
	s = case[1]
	p = case[2]
	scores = case[3:]

	for sc in scores:
		if (sc > (p-1)*3):
			answer+=1
		elif (sc > (p*3)-5 and s > 0 and sc >= 2 and sc <= 28):
			answer+=1
			s-=1

	ans.append(answer)
casefile.close()

outfile = open(wname, 'w')
caseno = 1

for i in ans:
	outfile.write("Case #%d: %d\n" % (caseno, i))
	caseno+=1

outfile.close()