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
	#print l
	cs = {}
	cs[l[0]] = 1
	next_i = -1
	for lii, lic in enumerate(l[1:]):
		if lic<>l[0]:
			cs[lic]=0
			next_i = lii+1
			break
	if next_i!=-1:
		max_d = 1
		for lii, lic in enumerate(l[next_i:]):
			if not cs.has_key(lic):
				max_d += 1
				cs[lic] =max_d
	#for i in range(len(l)):
	#	sys.stdout.write("%d" % cs[l[i]])
	#print ""
	s = 0; p = 1; base = len(cs)
	if base == 1: base = 2
	for i in range(len(l)-1, -1, -1):
		s += cs[l[i]]*p
		p *= base
	outstr = "Case #%d: %d" % (case_no, s)
	#print outstr
	fo.write(outstr);
	fo.write('\n');
	
f.close()
fo.close()

print "Done. written to %s"% outputfile

