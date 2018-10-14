import string
def altonum(x):
	d=ord
	return d(x)-d('a')
lines=3
text="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv""".split('\n')
textd="""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up""".split('\n')
lowl=list(string.ascii_lowercase)
pdict={}
for i in range(0,len(text)):
	for j in range(0,len(text[i])):
		pdict[text[i][j]]=textd[i][j]
pdict['q']='z'
pdict['z']='q'
ds={}
subbed=filter(lambda x:x not in pdict.keys(),lowl)
subbva=filter(lambda x:x not in pdict.values(),lowl)
srt=pdict.keys()
srt.sort()
#print 'subbed',subbed
#print 'subbva',subbva
#print len(srt)
#print map(lambda x:'{0}:{1}'.format(x,pdict[x]),srt)

lines=int(raw_input().strip())
def sanemap(x):
	if x not in pdict.keys():
		return x 
	return pdict[x]
for i in range(0,lines):
	print 'Case #{0}: {1}'.format(i+1,''.join(map(sanemap,raw_input())))