def mult(a,b):
	tabl={('1','i'):'i',
	('i','i'):'-1',
	('j','i'):'-k',
	('k','i'):'j',
	('-1','i'):'-i',
	('-i','i'):'1',
	('-j','i'):'k',
	('-k','i'):'-j',
	('1','j'):'j',
	('i','j'):'k',
	('j','j'):'-1',
	('k','j'):'-i',
	('-1','j'):'-j',
	('-i','j'):'-k',
	('-j','j'):'1',
	('-k','j'):'i',
	('1','k'):'k',
	('i','k'):'-j',
	('j','k'):'i',
	('k','k'):'-1',
	('-1','k'):'-k',
	('-i','k'):'j',
	('-j','k'):'-i',
	('-k','k'):'1'
	}
	return tabl[a,b]
t=int(raw_input())
for i in range(t):
	lent,rep=map(int,raw_input().split())
	l=raw_input()
	arr=""
	for j in range(rep):
		arr=arr+l
	flagi=0
	flagj=0
	curr="1"
	for j in range(lent*rep):
		curr=mult(curr,arr[j])
		if curr=="i" and flagi==0:
			flagi=1
			curr="1"
		if curr=="j" and flagj==0 and flagi==1:
			flagj=1
			curr="1"
	if curr=="k" and flagi==1 and  flagj==1:
		print "Case #"+ str(i+1)+": YES"
	else:
		print "Case #"+ str(i+1)+": NO"


