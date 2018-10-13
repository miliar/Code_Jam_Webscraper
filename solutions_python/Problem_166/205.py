import itertools as it

def tostr(ar):
	return ''.join([c for c in ar])

def cnt(sub, act):
	k=act
	c=0
	while k.count(sub) > 0:
		c+=1
		i=k.find(sub)
		k=k[i+1:]
	return c

t=input()
for tc in range(1, t+1):

	ans=0
	maxbans=0
	cnts=0
	tlbans=0


	k,l,s=map(int,raw_input().split())
	kb=raw_input()
	tar=raw_input()
	probs={let:kb.count(let) for let in kb}
	ovr=len(kb)

	for v in it.product(kb, repeat=s):
		perm=tostr(v)
		bans=cnt(tar, perm)
		maxbans=max(bans,maxbans)
		tlbans+=bans
		cnts+=1

	finbans=maxbans*cnts - tlbans
	ans=float(finbans)/cnts

	print "Case #%i: %f" % (tc, ans)