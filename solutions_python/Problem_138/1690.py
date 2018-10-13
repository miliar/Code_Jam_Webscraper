from copy import copy
def solve_war(n,_naomi,_ken):
	#for war
	score=0
	naomi=copy(_naomi)
	ken=copy(_ken)
	naomi.sort()
	ken.sort()
	for i in range(n):
		card_n=naomi[i]
		if card_n>ken[-1]:
			score+=1
			del ken[0]
		else:
			j=0
			while ken[j]<card_n:
				j+=1
			del ken[j]
	return score

def solve_deceit_war(n,_naomi,_ken):
	#for deceited war
	naomi=copy(_naomi)
	ken=copy(_ken)
	naomi.sort()
	ken.sort()
	compare=lambda x,y:(x-y)>0
	able=False
	i=0
	while able==False and i<n:
		if all(map(compare,naomi[i:],ken[:n-i])):
			able=True
		else:
			i+=1
	return n-i


m=input()
for i in range(1,m+1):
	n=input()
	_naomi=map(float,raw_input().split(' '))
	_ken=map(float,raw_input().split(' '))
	print 'Case #%d: %d %d'%(i,solve_deceit_war(n,_naomi,_ken),solve_war(n,_naomi,_ken))
