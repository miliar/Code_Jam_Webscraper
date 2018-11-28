def translate(a,dic):
	b=[]
	for i in a:
		b.append(dic[i])
	return ''.join(b)
def matcha(a,b,c):
	d=0
	for i in range(len(a)):
		if(c.has_key(a[i])):
			if(c[a[i]]!=b[i]):
				return 0
		else:
			c.setdefault(a[i],b[i])
a='ejp mysljylc kd kxveddknmc re jsicpdrysi'
b='rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
c='de kr kd eoya kw aej tysr re ujdr lkgc jvqz'
a1='our language is impossible to understand'
b1='there are twenty six factorial possibilities'
c1='so it is okay if you want to just give upzq'
aa=''.join([a,b,c])
bb=''.join([a1,b1,c1])
c={' ':' '}
matcha(aa,bb,c)
infile=file('A-small-attempt0.in','r')
T = int(infile.readline())
for t in range(1,T+1):
	l=infile.readline()
	ll=l.strip('\n')
	res=translate(ll,c)
	print "Case #%d: %s" % (t,res)
