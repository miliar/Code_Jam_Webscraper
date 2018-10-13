inp = open("Input.txt").readlines()
out = open("Output.txt",'w')

for j in range(int(inp[0].strip())):
	i = j*10
	ans1 = int(inp[i+1].strip())
	ans2 = int(inp[i+6].strip())

	row1 = inp[i+1+ans1].strip().split()
	row2 = inp[i+6+ans2].strip().split()

	found = 0
	for it in row1:
		if it in row2:
			ans = it
			found += 1

	if found==0:
		ans = "Volunteer cheated!"
	elif found>1:
		ans = "Bad magician!"

	out.write("Case #"+str(j+1)+": "+ans+"\n")

out.close()