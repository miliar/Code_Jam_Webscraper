num_cases=int(input())
all_data=[]
for i in range(num_cases):
	all_data.append(input())
# -------------------------------------------
case_count = 0
for i in range(num_cases):
	case_count = case_count+1
	nbr = str(all_data[i])
	nbr_array=[]
	for i in nbr:
		nbr_array.append(int(i))
		nbr_cnt = len(nbr_array)

	count = 0
	while  count < nbr_cnt:
		count  = count +1
		for i in range(1, nbr_cnt):
			if nbr_array[i] >= nbr_array[i-1]:
				pass
			else:
				nbr_array[i-1]  -=  1
				for j in range(i, nbr_cnt):
					nbr_array[j] = 9
	nbr_array_str=""
	for nbr_string in nbr_array:
		nbr_array_str+=str(nbr_string)

	print("Case #%d: %d" %(case_count, int(nbr_array_str)))
