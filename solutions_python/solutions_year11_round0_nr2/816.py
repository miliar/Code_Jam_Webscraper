import sys

def hash0(a,b):
	a = ord(a)
	b = ord(b)
	x = min(a,b)
	y = max(a,b)
	return x<<16 | y

def format_list(ls):
	s = '['
	for i,e in enumerate(ls):
		s += e
		if i < len(ls)-1:
			s+= ', '
	s +=']'
	return s

def process(fp):
	num_cases = int(fp.readline())
	for case in range(1,num_cases+1):
		line = fp.readline().replace('\n','')
		ls = line.split()
		#print line

		C = int(ls[0])
		pos = 1
		combine_rules = {}
		for i in range(C):
			s = ls[pos]
			combine_rules[hash0(s[0],s[1])] = (s[2],s[0],s[1])
			pos += 1

		D = int(ls[pos])
		pos += 1
		opposed_elements = {}
		for i in range(D):
			s = ls[pos]
			opposed_elements[hash0(s[0],s[1])]=(s[0],s[1])
			pos += 1


		N = int(ls[pos])
		pos += 1
		seq = ls[pos]
		#print 'C: %d, combine: %s, D: %d, opposed: %s, N: %d, invoked: %s' %(C, combine_rules, D, opposed_elements, N, seq)

		out = []

		for e2 in seq:
			#print '-----------'
			if len(out) == 0:
				#print 'appended: ', e2
				out.append(e2)
			else:
				e1 = out[-1]
				
				h = hash0(e1, e2)
				if h in combine_rules:
					e = combine_rules[h][0]
					#print 'combined: %s %s -> %s' % (e1, e2, e)
					del out[-1]
					out.append(e)
				else:
					found = False
					for prev in out:
						h = hash0(prev, e2)
						if h in opposed_elements:
							found = True
							#print 'clear %s %s' % (prev, e2)
							out = []
							continue
							#print out

					if not found:
						#print 'appended: ', e2
						out.append(e2)
						#print out

		print 'Case #%d:' % case, 
		print format_list(out)


if __name__ == '__main__':
	process(file(sys.argv[1]))
