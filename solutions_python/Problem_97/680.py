with open('C-large.out', 'w') as fout:
	with open('C-large.in', 'r') as fin:
		cnt=0		
		for line in fin:
			op_cnt=0
			if not cnt:
				cnt+=1
				continue
			line=line.strip()
			line_split = line.split(' ')
			A=int(line_split[0])
			B=int(line_split[1])
			if len(line_split[0])==1:
				fout.write("Case #" + str(cnt) + ": 0\n")
				cnt+=1
				continue
			for num in range(A,B+1):
				str_num=str(num)
				dig_cnt=-1
				list_rec = []
				for dig in range(0,len(str_num)):					
					recycle_part=str_num[dig_cnt:]
					recycle_num = recycle_part + str_num[:dig_cnt]
					int_recycle_num = int(recycle_num)
					if int_recycle_num>num:
						if int_recycle_num<=B:
							if int_recycle_num not in list_rec:
								list_rec.append(int_recycle_num)
								op_cnt+=1
					dig_cnt-=1
			fout.write("Case #" + str(cnt) + ": " + str(op_cnt) + '\n')
			cnt+=1