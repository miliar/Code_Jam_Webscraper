def	readint():
	return	(list(map(int,	sys.stdin.readline().strip().split(" "))))
def	readstr():
	return	(list(map(str,	sys.stdin.readline().strip().split("	"))))
def	rline():
	return	sys.stdin.readline().strip()
def	main():
	pass

if	__name__=='__main__':
	import	sys
	testcase	=	int(rline())
	for	i	in	range(testcase):
		l	=	readint()
		#print (l)
		n1	=	l[0]
		n2	=	l[1]
		li = []
		#print (n1, n2)
		for a in range(n1, n2+1):
			li.append(a)
		#print(li)
		dict = {}
		count = 0
		for ll in li:
			s = str(ll)
			lis = []
			for k in range(1, len(s)):
					s1 = s[len(s)-k:] + s[0:len(s)-k]
					if int(s1) in li and ll != int(s1):
						try:
							t = dict[ll]
						except KeyError:
							t = []
						t.append(int(s1))
						dict[ll] = t
						li.remove(int(s1))
		for e in dict:
			nn = len(dict[e])
			if nn == 1:
				count += 1
			else:
				count += nn * (nn+1) / 2
		print	('Case	#%d: %d'	%	((i+1),count))
	main()