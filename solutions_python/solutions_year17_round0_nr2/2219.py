num_count = input()

for i in range(1,num_count+1):
	num = raw_input()
	num_int = int(num)
	while num_int >= 0:
		found = True
		digit = int(num[0])
		for j in range(1, len(num)):
			if(int(num[j])>=digit):
				digit = int(num[j])
			else:
				found = False
				break
		if(found):
			break
		else:
			num_int -= 1
			num = str(num_int)

	print("Case #{}: {}".format(i,num_int))
