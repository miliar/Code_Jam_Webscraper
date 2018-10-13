
inf = open("A-large.in","r")

cases = int(inf.readline().strip("\n"))

outf = open("q1.out", "w")
for case in range (cases):
	line = inf.readline().strip("\n").split(" ")
	max_shy = int(line[0])
	shyness = list(map(int,line[1]))

	ans = 0
	tot =0

	for i in range (max_shy+1):
		if tot<i:
			diff = i-tot
			ans += diff
			tot += diff
		tot+=shyness[i]

	outf.write("Case #%d: %d\n" % (case+1,ans))
