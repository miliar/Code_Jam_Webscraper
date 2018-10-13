




def f1(list1):
	C=list1[0]
	F=list1[1]
	X=list1[2]
	R=2
	total=0
	while True:
		if X/R < (C)/R+(X/(R+F)):
			total+=X/R
			break
		else:
			total+=C/R
			R=R+F
	return total





if __name__=="__main__":
	n=int(raw_input())
	temp=[]
	for i in xrange(0,n):
		l1=raw_input().split(' ')
		l1=[float(x) for x in l1]
		temp.append(l1)
	for i in xrange(1,len(temp)+1):
		print 'Case #%d: %f'%(i,f1(temp[i-1]))
	
