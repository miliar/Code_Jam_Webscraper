import sys

if __name__ == "__main__":
	nb = int(sys.stdin.readline())
	cpt = 1
	
	while cpt <= nb:
		a, b = sys.stdin.readline().replace('\n', '').split(' ')
		ia = int(a)
		ib = int(b)
		total = 0
		l = []

		if(len(a) == 1 or len(b) == 1):
			total = 0
		else:
			s = a
			while int(s) < ib:
				before = s
				after = s
				for i in range(len(s)-1):
					after = after[len(s)-1]+after[0:len(s)-1]
					value = int(after)
					if value > ia and value <= ib and value > int(s):
						total += 1
						if l.count((before, after)) == 0:
							l.append((before, after))
						
						
				s = str(int(before)+1)
				
		print 'Case #'+str(cpt)+': '+str(len(l))
	
		cpt += 1
	