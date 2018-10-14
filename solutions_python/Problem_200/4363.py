t = int(input().strip())
for x in range(t):
	n = input()
	check = 0
	if len(n)==1:
		print("Case #",x+1,": ",n,sep="")
		continue
	ans = n
	for i in range(len(n)-1):
		if n[i]>n[i+1]:
			check=1
			break
	if check == 1:
		for i in range(len(n)-1):
			if n[i]>=n[i+1]:
				ans = n[:i]+str(int(n[i])-1)+"9"*(len(n)-i-1)
				break
	print("Case #",x+1,": ",ans.replace("0"," ").strip(),sep="")


		



