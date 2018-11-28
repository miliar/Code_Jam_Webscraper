num_count = input()

for i in range(1,num_count+1):
	input = raw_input().split()
	num_userstalls = int(input[0])
	num_people = int(input[1])

	y_max = 0
	z_min = 0

	while(True):
		if(num_people == 1):
			num_userstalls -= 1
			break
		
		if(num_people % 2 == 0):
			num_userstalls /= 2
			num_people /= 2
			continue

		if(num_userstalls % 2 == 0):
			num_userstalls = num_userstalls / 2 - 1
			num_people /= 2
			continue
		
		num_userstalls /= 2
		num_people /= 2

	if(num_userstalls % 2):
		
		y_max = (num_userstalls+1)/2
		z_min = (num_userstalls-1)/2
	else:
		y_max = num_userstalls/2
		z_min = y_max
	
	print("Case #{}: {} {}".format(i,y_max,z_min))

