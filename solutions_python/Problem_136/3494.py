import sys

# inf = open("input", 'r')
# outf = open("output", 'w')
inf = open(sys.argv[1], 'r')
outf = open(sys.argv[2], 'w')

case = 1
with inf as f:
    next(f)
    for line in f:
		line = [float(x) for x in line.strip().split()]
		# print line
		C = line[0]
		F = line[1]
		X = line[2]

		res = sys.maxint
		res_p = sys.maxint

		kFarm = 0
		while res <= res_p:
			kT = 0
			res_p = res
			for i in xrange(0,kFarm):
				kT += 1.0/(2+i*F)
			kT = kT*C
			res = kT+(X*1.0)/(2+kFarm*F)
			kFarm+=1
		res = "%.15f"%res_p
		output = str(res)
		output = "Case #"+str(case)+": "+output+'\n'
		outf.write(output)
		case+=1

inf.close()
outf.close()

