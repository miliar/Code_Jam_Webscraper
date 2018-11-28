
import sys
fp = open(sys.argv[1])
lines = fp.readlines()

linenum=0
totcase = int(lines[0].strip())
for line in lines[1:]:
	linenum += 1
	if linenum % 2 == 1:
		line = line.strip().split()
		typed = int(line[0])
		total = int(line[1])
	if linenum % 2 == 0:
		expect = []
		poss = line.strip().split()
		if typed == 1:
			poss = poss[0]
			expect.append(float(poss)*total+(1-float(poss))*(2*total+1))
			expect.append(total+2)
		elif typed == 2:
			poss1 = float(poss[0])
			poss2 = float(poss[1])
			expect.append(poss1*poss2*(total-1) + (1-poss1*poss2)*(2*total))
			expect.append(poss1*(total+1) + (1-poss1)*(2*total+3))
			expect.append(total+2)
		elif typed == 3:
			poss1 = float(poss[0])
			poss2 = float(poss[1])
			poss3 = float(poss[2])
			expect.append(poss1*poss2*poss3*(total-2) + (1-poss1*poss2*poss3)*(2*total-1))
			expect.append(poss1*poss2*(total) + (1-poss1*poss2)*(2*total+1))
			expect.append(poss1*(total+2) + (1-poss1)*(total+3))
			expect.append(total+2)
			
		print "Case #%d: %.6f" % (linenum / 2, min(expect))
