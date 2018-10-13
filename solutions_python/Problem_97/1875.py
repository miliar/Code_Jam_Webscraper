#!/usr/bin/python2
#from itertools import permutations
def permutations(l):
	return set([l[i:]+l[:i] for i in range(len(l))])
instr=open('C-small-attempt0.in','r').read()
#instr=open('C.in','r').read()
instr=instr.split('\n')
instr=map(lambda x:x.split(),instr)
instr=map(lambda x:map(int,x),instr)
#print instr
for i,e in list(enumerate(instr[:-1]))[1:]:
	thelist=range(e[0],e[1])
	answer=0
	for n in thelist:
	#	if n<10:
	#		continue
	#	print list(permutations(str(n)))
	#	print map(lambda x:"".join(x),list(permutations(str(n))))
		perms=[m for m in map(lambda x:int("".join(x)),permutations(str(n))) if (n<m<=e[1])]
		for m in perms:
			#print m
			try: thelist.remove(m)
			except ValueError: pass
		answer+= (len(perms)*(len(perms)+1))/2
	print 'Case #' +str(i)+":",answer
