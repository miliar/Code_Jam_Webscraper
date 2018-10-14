import sys
readline = sys.stdin.readline

if __name__ == "__main__":
	for i in range(1, int(readline())+1):
		engs = []
		for j in range (int(readline())):
			engs.append (readline().strip())
		#print engs
		
		opts=set(engs)
		numsw = 0
		for j in range (int(readline())):
			q = readline().strip()
			opts.discard (q)
			if not opts:
				opts = set(engs)
				opts.discard (q)
				numsw +=1
		
		print "Case #%d: %s" % (i, numsw)