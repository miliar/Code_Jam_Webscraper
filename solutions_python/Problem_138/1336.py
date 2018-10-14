

def war(n, k):
	n = sorted(n)
	k = sorted(k)

	
	l = len(n)
	while len(k) != 0:
		if k[0] > n[0]:
			k.pop(0)
			n.pop(0)
		else:
			k.pop(0)


	return len(n)





def d_war(n, k, l):
	n = sorted(n)[::-1]
	k = sorted(k)

	pt = 0
	for i in xrange(l):
		if k[-1] > n[0]:
			k.pop()
			n.pop()
		else:
			k.pop(0)
			n.pop(0)
			pt += 1
			print 'win'
		print n
		print k
		print

	return pt
	



def main():
	for case in xrange(1, input()+1):
		blocks = input()

		n = map(float, raw_input().split(" "))
		k = map(float, raw_input().split(" "))
		
		print "Case #%d: %d %d" % (case, blocks-war(k,n), war(n, k)) 

main()