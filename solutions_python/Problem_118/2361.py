import math
T=input();
for i in range(T):
	X=raw_input();
	X=X.split();
	A=X[0];
	B=X[1];
	a=int(A);
	b=int(B);
	count=0;
	for j in range(a,b+1):
		string=str(j);
		string1=string[::-1]
		if string==string1:
			temp=math.sqrt(j);
			temp=int(temp);
			if temp*temp==j:
				string=str(temp);
				string1=string[::-1]
				if string==string1:
					count+=1;
	print "Case #"+str(i+1)+": "+str(count);
