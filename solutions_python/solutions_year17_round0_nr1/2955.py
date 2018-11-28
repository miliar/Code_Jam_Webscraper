with open("input.in") as file_in, open("output.out", "w+t") as output_file:
	tests = int(file_in.readline())
	result = []
	count = 1
	for i in file_in:
		list_input = i.split(' ')
		flips = 0
		cakes = [1 if(c == '+') else 0 for c in list_input[0]]
		flipper = int(list_input[1])
		if(sum(cakes) == len(cakes)):
			output_file.write("Case #{}: {}\n".format(count,0))
		elif(len(cakes) < flipper):
			output_file.write("Case #{}: {}\n".format(count,"IMPOSSIBLE"))
		else:
			count_cake = 0
			while(count_cake<len(cakes)):
				if(cakes[count_cake] == 0):
					flips += 1
					if((count_cake+flipper-1) < len(cakes)):
						for f in range(flipper):
							cakes[count_cake+f] = abs(cakes[count_cake+f]-1)
				
				count_cake += 1
			if(sum(cakes) != len(cakes)):
				output_file.write("Case #{}: {}\n".format(count,"IMPOSSIBLE"))
			else:
				output_file.write("Case #{}: {}\n".format(count,flips))
			
		count += 1 
		