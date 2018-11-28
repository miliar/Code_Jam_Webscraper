import sys

args = sys.argv[1:]

inputfile = args[0]
outputfile = inputfile+'.out'

T='welcome to code jam'
TU=''.join(list(set(T)))
print TU
TLEN = len(T)

f = open(inputfile)

l1 = f.readline().strip()
print l1
N = int(l1)
fo = open(outputfile, 'w')
case_no = 0
for n in range(N):
	l = f.readline().rstrip('\r\n')
	case_no += 1
	count = 0
	llen = len(l)
	if llen>=TLEN:
		allfound=True
		for tui in TU:
			if tui not in l:
				allfound = False
				break
		if allfound:
			# dynamic programming
			mp = [0]*TLEN # count of 'w', 'we',  'wel', ... T occurring before current pos
			for lv in l:
				m = [None]*TLEN
				if lv==T[0]:
					m[0] = mp[0]+1
				else:
					m[0] = mp[0]
				for mpi in range(1, TLEN):
					# assume no two consequtive chars in T are the same
					
					# if don't consider current char
					m[mpi] = mp[mpi]
					if lv==T[mpi]:
						# also can consider current char
						m[mpi] = (m[mpi] + mp[mpi-1]) % 10000
				mp = m
			count = m[TLEN-1]		
	fo.write('Case #%d: %04d\n' % (case_no, count))
	
f.close()
fo.close()

print "Done. written to %s" % outputfile
