Python 2.7.2 (default, Jun 12 2011, 14:24:46) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ot=open('out.txt','w')
>>> f=open('C-small-attempt1.in')
>>> for idx in range(int(f.readline())):
	A,B=f.readline().split()
	A=int(A)
	B=int(B)
	cnt=0
	for val in range(A,B+1):
		str_val=str(val)
		i=0
		for num in str_val[1:]:
			i=i+1
			if int(num)!=0 and int(str_val)<int(str_val[i:]+str_val[:i]) and int(str_val[i:]+str_val[:i])<=B:
				cnt=cnt+1
	ot.write('Case #%d: %d\n' %(idx+1,cnt))

	
>>> ot.close()
>>> 
