L = int(raw_input())
for l in xrange(L):
	tree_s = ""
	A = int(raw_input())
	for a in xrange(A):
		s = raw_input()
		s = s.replace('(', '[ ')
		s = s.replace(')', ' ]')
		sl = s.split()
		for e in sl:
			if tree_s!="" and e!=']' and (tree_s[-1]=="'" or tree_s[-1]=="]"): tree_s+=","
			if e!='[' and e!=']':
				tree_s+="'"+e+"'"
			else: tree_s+=e
	tree = eval(tree_s)
	#print tree
	n = int(raw_input())
	print "Case #%d:" % (l+1)
	for a in xrange(n):
		anim = raw_input().split()[2:]
		where = tree
		p = 1
		#print anim
		found = False
		while (found==False):
			#print "Where: ", where
			p = p*float(where[0])
			if len(where)==1: break
			if (where[1] in anim): where = where[2]
			else: where = where[3]
		print "%.7f" % (p)
	
