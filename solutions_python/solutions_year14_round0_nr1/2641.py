for case in range(eval(input())):
	r1n = eval(input())-1
	for i in range(4):
		if i==r1n:
			r1 = input().split(" ")
		else:
			input()

	r2n = eval(input())-1
	for i in range(4):
		if i==r2n:
			r2 = input().split(" ")
		else:
			input()

	values = list(set(r1) & set(r2))
	print("Case #", case+1, ": ", sep="", end="")

	if len(values)>1:
		print("Bad magician!")
	elif len(values)==0:
		print("Volunteer cheated!")
	else:
		print(values[0])