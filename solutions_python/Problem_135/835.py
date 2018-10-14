'''
Magic Trick
'''

if __name__ == '__main__':
	f=open("A-small-attempt1.in")
	nc=int(f.readline())
	for x in xrange(1,nc+1):
		c1=int(f.readline())
		a1=[]
		for i in range(4):
			l=f.readline().strip('\n')
			r=l.split(' ')
			a1.append(r)
		c2=int(f.readline())
		a2=[]
		for i in range(4):
			l=f.readline().strip('\n')
			r=l.split(' ')
			a2.append(r)
		intt = list(set(a1[c1-1]) & set(a2[c2-1]))
		ll=len(intt)
		if ll == 1:
			print "Case #%d: %s" % (x, intt[0])
		elif ll > 1:
			print "Case #%d: %s" % (x, "Bad magician!")
		else:
			print "Case #%d: %s" % (x, "Volunteer cheated!")
			
