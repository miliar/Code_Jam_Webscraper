c=input().strip()
for q in range(int(c)):
	a,b,k=input().strip().split()
	result=0
	for i in range(int(a)):
		for j in range(int(b)):
			if (i&j)<int(k):
				result+=1
	print("Case #",q+1,": ", result, sep='')