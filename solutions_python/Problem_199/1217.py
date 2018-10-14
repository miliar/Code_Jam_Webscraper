t=int(input())
for i in range(t):
	cont=0
	pancakes,k=input().split()
	flip=int(k)
	pan=list(pancakes)
	for j in range(len(pan)-flip+1):
		if pan[j]=="-":
			cont+=1
			for l in range(j,j+flip):
				if pan[l]=="+":
					pan[l]="-"
				else:
					pan[l]="+"
	possible=(pan.count("+")==len(pan))
	if possible:
		print("Case #{}: {}".format(i+1, cont))
	else:
		print("Case #{}: IMPOSSIBLE".format(i+1))