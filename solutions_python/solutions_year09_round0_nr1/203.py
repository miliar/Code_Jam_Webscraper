import re
q=re.compile("\(|\)")
def genMatches(p,c=None,r=None,w=True):
	if not c: c=re.split(q,p)
	if not r: r=[""]
	if w: r=[v+c[0] for v in r]
	else:
		tmp = []
		for g in r: tmp += [g+f for f in list(c[0])]
		r=tmp
	return r, c[1:]

def genPrefixes(s): return [s[0:i] for i in xrange(1,len(s)+1)]

(l, d, n) = raw_input().split(" ")
e={}
b={}
for x in xrange(0,int(d)): 
	m=raw_input()
	for y in genPrefixes(m): b[y]=1
	e[m]=1

for x in xrange(0,int(n)):
	m=raw_input()
	n=genMatches(m)
	w=False
	while n[1] != []:
		u=filter(lambda k: k in b, n[0])
		n=genMatches(q,n[1],u,w)
		w=not w
	print "Case #"+str(x+1)+":",len(filter(lambda y: y in e, n[0]))


