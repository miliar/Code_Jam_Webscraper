for x in range(int(input())):
	i = list(input())
	r = 0
	while r < len(i)-1:
		if (int(i[r]) > int(i[r + 1])):
			i[r] = str(int(i[r])-1)
			for z in range(r+1, len(i)):
				i[z] = "9"
			if(r != 0) and (i[r] < i[r-1]):
				r = -1
		r = r+1
	print("Case #{0}: {1}".format(str(x+1), int("".join(i))))