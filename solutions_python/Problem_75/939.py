
import sys


def solve(line):
	line=line.split()
	#print line	
	i=0
	
	C=int(line[i])
	i+=1
	comb=[['#']*100 for j in xrange(100)]
	
	for j in xrange(C):
		t=line[i]
		comb[ord(line[i][0])][ord(line[i][1])]=line[i][2]
		comb[ord(line[i][1])][ord(line[i][0])]=comb[ord(line[i][0])][ord(line[i][1])]				
		i+=1
		
	D=int(line[i])
	i+=1
	opp={}
	for j in xrange(D):		
		t=line[i]
		if t[0] not in opp:
			opp[t[0]]=set()
		opp[t[0]].add(t[1])
		
		if t[1] not in opp:
			opp[t[1]]=set()
		opp[t[1]].add(t[0])		
		
		i+=1
		
	N=int(line[i])
	i+=1
		
	ans=[]	
		
	for e in line[i]:
		#print e
		if len(ans)>0 and comb[ord(e)][ord(ans[-1])]!='#':
			ans[-1]=comb[ord(e)][ord(ans[-1])]
		else:
			cleared=False
			for a in ans:
				if a in opp.get(e,[]):
					ans=[]
					cleared=True
					break
			if not cleared:
				ans.append(e)
				
	return ans
	

if __name__=="__main__":
	tcases=input()
	
	for tcase in xrange(1,tcases+1):
		line=sys.stdin.readline()
		print 'Case #%d: ['%(tcase),
		
		sol=solve(line)
		for i in xrange(len(sol)):
			a=sol[i]
			sys.stdout.write('%s'%a)
			if i<len(sol)-1:
				sys.stdout.write(', ')
		sys.stdout.write(']\n')
				
		
