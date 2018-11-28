import sys

inf = open(sys.argv[1], 'r')
# inf = open("A-small-attempt0.in", 'r')
outf = open(sys.argv[2], 'w')
# outf = open("output", 'w')

times = 0
case = 1
caseDic = []
with inf as f:
    next(f)
    for line in f:
		line = [int(x) for x in line.strip().split()]
		# print line
		num = len(line)
		if num == 1:
			myline = int(line[0])
			times+=1
		
		myline-=1
		if myline == -1:
			# print line
			caseDic.append(set(line))
		else:
			continue

		if times == 2:
			# print case
			res = caseDic[0].intersection(caseDic[1])
			# print res
			resLen = len(res)
			if resLen == 1:
				output = str(res.pop())
			elif resLen == 0:
				output = "Volunteer cheated!"
			elif resLen > 1:
				output = "Bad magician!"		

			output = "Case #"+str(case)+": "+output+'\n'
			outf.write(output)

			times = 0
			caseDic = []
			case+=1
inf.close()
outf.close()
