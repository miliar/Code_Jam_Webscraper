t = int(input())
for i in range(t):
	n = int(input());
	while(n>=1):
		str1 = list(map(int,list(str(n))));
		if(sorted(str1) == str1):
			print("Case #" + str(i+1) + ": " + ''.join(map(str,str1)))
			break;

		n = n-1;


