import math

def servePancakes(diners,level):

	diners.sort()
	splits = 0

	if max(diners) <= 0:
		return 0
	if(diners[-1] < len(diners)):
		return 1 + servePancakes([(x - 1) for x in diners], level + 1)
	else:
		if diners[-1] >= 4:
			best = max(diners)
			for s in range(1,int(math.sqrt(diners[-1]))):
				add = [diners[-1]//(s+1) for x in range(0,s)]
				tVal = s + servePancakes(diners[:-1] + [diners[-1] - sum(add)] + add, level + 1)
				if tVal < best:
					best = tVal
			return best
		else:
			return max(diners)

filename_in = 'B-small-attempt0.in'
filename_out = 'B-small-attempt0.out'

fin = open(filename_in,'r')
fout = open(filename_out,'w')

print(int(fin.readline()))
casenum = 0

arrayNum = True
for l in fin:
	if arrayNum:
		arrayNum = False
	else:
		arrayNum = True
		s = l.split(' ')
		s = [int(x) for x in s]
		casenum += 1
		fout.write('Case #' + str(casenum) + ': ' + str(servePancakes(s,1)) +'\n')


fin.close()
fout.close()