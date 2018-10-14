t = int(input())
for i in range(t):
	ans1 = int(input())
	grid1 = []
	for j in range(4):
		grid1.append(input())
	ans2 = int(input())
	grid2 = []
	for j in range(4):
		grid2.append(input())
	count = 0
	ans = "";
	for val in grid1[ans1-1].split():
		 if val in grid2[ans2-1].split():
		 	count += 1;
		 	ans = val;
	if count == 0:
		print("Case #"+str(i+1)+": Volunteer cheated!")
	elif count == 1:
		print("Case #"+ str(i+1)+":", ans)
	else:
		print("Case #"+str(i+1)+": Bad magician!")
		