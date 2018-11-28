# -- separate project  --BASE FILE for comp-----------
def readint(): return int(f.readline())
def readarray(): return [int(x) for x in f.readline()[:-1].split()]

def fun():
	R=readint(); v=[]
	for i in xrange(1,5):
		if i==R: v=readarray()
		else: readarray()
	R1=readint(); v1=[]
	for i in xrange(1,5):
		if i==R1: v1=readarray()
		else: readarray()
	result=[]
	for i in v:
		if i in v1: result.append(i)
	if len(result)==0: return 'Volunteer cheated!'
	if len(result)>1: return 'Bad Magician!'
	return result[0]



f=open('in','r');T=readint()
for i in range(1,T+1):
    print "Case #%d: %s" %(i,fun())