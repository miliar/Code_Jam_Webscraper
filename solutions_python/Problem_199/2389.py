num_cases = int(input())
for case in range(num_cases):
	pancakes_arr_input = input()
	input_list = pancakes_arr_input.split()
	flipper = int(input_list[1])
	pancakes_arr = list(input_list[0])
	flip =0
	length = len(pancakes_arr)
	flag =0
	
	for x in range(len(pancakes_arr)):
		if pancakes_arr[x] == '-':
			#print(pancakes_arr)
			if length - x >= flipper:
				#print('inside first-second loop' + pancakes_arr)	
				flip = flip +1
				for k in range(flipper):
					if pancakes_arr[x+k] == '-':
						pancakes_arr[x+k] = '+'
					elif pancakes_arr[x+k] == '+':
						pancakes_arr[x+k] = '-'
			else:
				#print('inside else loop'+pancakes_arr)
				flag =1 
				break

	#print(flag)
	if flag == 1:
		#print (pancakes_arr)
		print("Case #{}: {}".format(case+1, 'IMPOSSIBLE'))
	else:
		print("Case #{}: {}".format(case+1, flip))






