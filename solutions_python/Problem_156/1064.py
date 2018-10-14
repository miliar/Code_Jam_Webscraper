def optimalNbr(inpt):
	max_value = 0
	i = 0
	for index, value in enumerate(inpt):
		if value > max_value:
			i = index
			max_value = value

	if(max_value <=3 ):
		return max_value
	else:
		cost = max_value
		for j in range(2,int(max_value/2)+1):
			new_list = inpt.copy()
			new_list[i] = j
			new_list.append(max_value-j)
			n = 1+optimalNbr(new_list)

			if n<cost :
				cost = n

		return cost

if __name__ == "__main__":

	with open("input") as f:
		f.readline()
		f.readline()
		i = 1
		for line in f:
			disp = line.split("\n")[0].split(" ")#[0:len(line)-1]
			disp = [int(x) for x in disp]
			#print(disp)
			f.readline()
			#disp = shyness_array[:len(shyness_array)-1]
			print("Case #"+str(i)+": "+str(optimalNbr(disp)))
			i = i+1