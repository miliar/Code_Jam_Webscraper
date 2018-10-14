with open('B-large.out', 'w') as fout:
	with open('B-large.in', 'r') as fin:
		cnt=0		
		for line in fin:
			op_cnt=0
			if not cnt:
				cnt+=1
				continue
			line=line.strip()
			line_split = line.split(' ')
			no_googlers_N = line_split[0]
			no_googlers_N = int(line_split[0])
			no_surp_S = int(line_split[1])
			no_best_P = int(line_split[2])
			list_tot = line_split[3:]
			for tot in list_tot:
				new_tot = int(tot)
				sub_cnt = 0
				while new_tot%3:
					sub_cnt+=1
					new_tot-=1
				j1=new_tot/3
				if sub_cnt==1:
					j1+=1
				elif sub_cnt==2:
					if j1==9:
						j1+=1;
					elif no_surp_S:
						if (j1+1)>=no_best_P:
							op_cnt+=1
							continue
						elif (j1+2)>=no_best_P:
							op_cnt+=1
							no_surp_S-=1
							continue
					else:
						j1+=1
				elif sub_cnt==0:
					if j1>=no_best_P:
						op_cnt+=1
						continue;
					elif no_surp_S and new_tot>0:
						if (j1+1)>=no_best_P:
							op_cnt+=1
							no_surp_S-=1
							continue;
				if j1>=no_best_P:
					op_cnt+=1
			fout.write("Case #" + str(cnt) + ": " + str(op_cnt) + '\n')
			cnt+=1