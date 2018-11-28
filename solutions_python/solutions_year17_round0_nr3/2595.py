cases = int(input())

res = []

for case in range(cases):
	stalls, people = input().split(' ')
	people = int(people)
	stalls = int(stalls)
	tmp = 'O'+'.'*stalls+'O'
	const = tmp
	
	flag = 0

	if stalls==people:
		res.append((0, 0))
		continue

	for person in range(people):
		flag = 0
		tmp = sorted(tmp.split('O'), reverse=True)[0]
		pos = const.find(tmp)
		amount_of_elements = len(tmp)
		if amount_of_elements%2:
			middle_of_main_list = len(tmp)//2
		else:
			middle_of_main_list = len(tmp)//2-1
		tmp=list(tmp)
		const = list(const)

		if const[middle_of_main_list+pos-1]=='O' and const[middle_of_main_list+pos+1]=='.' and middle_of_main_list+pos!=1:
			const[middle_of_main_list+pos+1]='O'
			flag = 1
		else:
			const[middle_of_main_list+pos]='O'
			flag = 2

		const = ''.join(const)
		tmp = const

	if flag == 1:
		tmp_pos = middle_of_main_list+pos+1
	else:
		tmp_pos = middle_of_main_list+pos

	counter = 1
	# left
	while True:
		if const[tmp_pos-counter]=='O':
			tmp_min=counter-1
			break
		counter+=1

	counter = 1
	# right
	while True:
		if const[tmp_pos+counter]=='O':
			tmp_max=counter-1
			break
		counter+=1

	tmp_min, tmp_max = sorted([tmp_max, tmp_min])
	res.append((tmp_max, tmp_min))

for pos, i in enumerate(res, start=1):
	print('Case #{}: {} {}'.format(pos, i[0], i[1]))