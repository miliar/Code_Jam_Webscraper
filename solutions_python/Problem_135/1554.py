# Magus Verma
t = int(input())
for case in range(1,t+1):
	f = input()
	fa = []
	for i in range(4):
		fa.append([int(x) for x in raw_input().split()])
	l = input()
	la = []
	for i in range(4):
		la.append([int(x) for x in raw_input().split()])
	ans = [val for val in fa[f-1] if val in la[l-1]]
	
	if(len(ans)==1):
		ans = str(ans[0])
	elif(len(ans)>1):
		ans = "Bad magician!"
	else:
		ans = "Volunteer cheated!"
	print("Case #{}: {}".format(case, ans))