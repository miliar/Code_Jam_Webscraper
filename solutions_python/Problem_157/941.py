def main():
	f=open("C.in")
	T=int(f.readline())
	for x in range(T):
		print "Case #"+str(x+1)+":",
		L,X=map(int,f.readline().split())
		string=map(str,f.readline())
		string.remove('\n')
		if len(set(string))==1:
			print "NO"
			continue
		string=string*X
		if possible(string):	print "YES"
		else:	print "NO"

def possible(X):
	Table={	
		('1','1'):'1',
		('1','i'):'i',
		('1','j'):'j',
		('1','k'):'k',
		
		('i','1'):'i',
		('i','i'):'-1',
		('i','j'):'k',
		('i','k'):'-j',
		
		('j','1'):'j',
		('j','i'):'-k',
		('j','j'):'-1',
		('j','k'):'i',
		
		('k','1'):'k',
		('k','i'):'j',
		('k','j'):'-i',
		('k','k'):'-1',
		
		('-1','1'):'-1',
		('-1','i'):'-i',
		('-1','j'):'-j',
		('-1','k'):'-k',
		
		('-i','1'):'-i',
		('-i','i'):'1',
		('-i','j'):'-k',
		('-i','k'):'j',
		
		('-j','1'):'-j',
		('-j','i'):'k',
		('-j','j'):'1',
		('-j','k'):'-i',
		
		('-k','1'):'-k',
		('-k','i'):'-j',
		('-k','j'):'i',
		('-k','k'):'1',
		
		('1','-1'):'-1',
		('1','-i'):'-i',
		('1','-j'):'-j',
		('1','-k'):'-k',
		
		('i','-1'):'-i',
		('i','-i'):'1',
		('i','-j'):'-k',
		('i','-k'):'j',
		
		('j','-1'):'-j',
		('j','-i'):'k',
		('j','-j'):'1',
		('j','-k'):'-i',
		
		('k','-1'):'-k',
		('k','-i'):'-j',
		('k','-j'):'i',
		('k','-k'):'1',
		
		('-1','-1'):'1',
		('-1','-i'):'i',
		('-1','-j'):'j',
		('-1','-k'):'k',
		
		('-i','-1'):'i',
		('-i','-i'):'-1',
		('-i','-j'):'k',
		('-i','-k'):'-j',
		
		('-j','-1'):'j',
		('-j','-i'):'-k',
		('-j','-j'):'-1',
		('-j','-k'):'i',
		
		('-k','-1'):'k',
		('-k','-i'):'j',
		('-k','-j'):'-i',
		('-k','-k'):'-1',
		}

	m='1'
	n='1'
	a=b=0
	for i in range(len(X)):
		if a==1:	n=Table[n,X[i]]
		if n=='j':	b=1
		m=Table[m,X[i]]
		if m=='i':	a=1
	if m=='-1'and a==1 and b==1:	return True
	return False

if __name__=='__main__':
	main()