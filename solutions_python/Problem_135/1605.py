f = file("A-small-attempt1.in")
g = file("output.txt", "w")
arr_in = f.read().split('\n')
for case in range(int(arr_in[0])):
	solution = set(arr_in[int(arr_in[case*10+1])+case*10+1].split()) & set(arr_in[int(arr_in[case*10+6])+case*10+6].split())
	out = ""
	if len(solution) >= 2:
		out = "Bad magician!"
	elif len(solution) == 1:
		(out,) = solution
	else: out = "Volunteer cheated!"
	g.write("Case #"+str(case+1)+": "+out+"\n")