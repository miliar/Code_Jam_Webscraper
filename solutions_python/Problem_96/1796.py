import sys

def possible(triplet):
	return(max(triplet)-min(triplet)<=2)

def checkall(total):
	a=[]
	for i in range(total+1):
		for j in range(i+1):
			if possible({i,j,total-i-j}):
				a.append({i,j,total-i-j})
	return a;	


def surprising(triplet):
	return(max(triplet)-min(triplet)==2)

def goodsurprising(l,S):
	c=0
	for el in l:
		if surprising(el): c=c+1
	return c==S

def Countlargebest(el,p):
	c=0
	for a in el:
		if max(a)>=p:
			c=c+1
	return c

	
if __name__ == "__main__":

	f=sys.stdin
	f=sys.argv[1]
	myfile=open(f)
	T=int(myfile.readline())
	for i in range(T):
		line=myfile.readline().split()
		N=int(line[0])
		S=int(line[1])
		p=int(line[2])
		totals=line[3:]
		possibilities=[checkall(int(total)) for total in totals]
		game=[{0,0,0} for t in range(N)]
		initial=[game]
		for k in range(len(possibilities)):
			final=[]
			for f in initial:
				for el in possibilities[k]:
					f1=[u for u in f]
					f1[k]=el
					final.append(f1)
			initial[:]=final[:]
		MaxNumber=0
		for element in final:
			if goodsurprising(element,S):
				M=Countlargebest(element,p)
				if MaxNumber<M:
					MaxNumber=M			

		print "Case #"+str(i+1)+":",MaxNumber
			
