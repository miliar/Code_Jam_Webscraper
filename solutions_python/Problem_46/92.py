import sys

args = sys.argv[1:]

inputfile = args[0]
outputfile = inputfile+'.out'

f = open(inputfile)

l1 = f.readline().strip()
print l1
T = int(l1)


fo = open(outputfile, 'w')
case_no = 0
for i in range(T):
	case_no += 1
	l = f.readline().rstrip('\r\n')
	N = int(l)
	m = [-1]*N
	for n in range(N):
		l = f.readline().rstrip('\r\n')
		ni = N-1
		while ni>=0:
			if l[ni]=='1':
				m[n]=ni
				break
			ni -= 1
	count = 0
	for ni,nv in enumerate(m):
		if nv>ni:
			# need to move one from below to here
			for nii in range(ni+1, N):
				if m[nii]<=ni:
					tmp = m[nii]
					for niii in range(nii, ni, -1):
						m[niii] = m[niii-1]
					m[ni] = tmp
					count += (nii-ni)
					break
	#print l
	outstr = "Case #%d: %d" % (case_no, count)
	#print outstr
	fo.write(outstr);
	fo.write('\n');
	
f.close()
fo.close()

print "Done. written to %s"% outputfile

