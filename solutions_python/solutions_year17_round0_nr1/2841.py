num_cases=int(input())
all_data=[]
for i in range(num_cases):
	all_data.append(input())

case_count = 0
for i in range(num_cases):
	case_count = case_count+1
	pnc = all_data[i]
	# ------------------------------------------
	pnc_s = pnc.split(' ')[0]
	pnc_k = int(pnc.split(' ')[1])
	pnc_array=[]
	for i in pnc_s:
		pnc_array.append(i)
	pnc_cnt = len(pnc_array)
	count = 0
	for i in range(0, pnc_cnt):
		if  pnc_array[i] == "-":
			count=count+1
			for j in range(i, pnc_k+i):
				if pnc_cnt >= (pnc_k+i):
					if  pnc_array[j] == "-":
						pnc_array[j] = "+"
					else:
						pnc_array[j]="-"
				else:
					pass
		else:
			pnc_array[i] == "+"
	if '-' in pnc_array:
		count="IMPOSSIBLE"
	print("Case #%d: %s" %(case_count, str(count)))
