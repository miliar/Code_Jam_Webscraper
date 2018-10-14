def is_sorted(l):
    return all(a <= b for a, b in zip(l[:-1], l[1:]))

print("\n")
n=int(input().strip())
for i in range(n):
	a=int(input().strip())
	for j in range(a,0,-1):
		l=[]
		l=[int(k) for k in str(j)]
		print
		if(is_sorted(l)):
			print("Case #"+str(i+1)+":",j)
			break
			
