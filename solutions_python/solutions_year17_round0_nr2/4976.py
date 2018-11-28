output_list=[]
with open(r'E:\GoogleCodeJam2017\tidynumbers\B-small-attempt2.in','r') as f:
	t=int(f.readline().strip())
	for i in range(t):
		n=int(f.readline().strip())
		for j in range (n):
			#j will be 0 to n-1
			num=j+1
			# convert to string
			str_num=str(num)
			# sort string in ascending order
			ascending_str = "".join(sorted(str_num))
			# compare them
			if str_num == ascending_str :
				last_tidy = num
		output_line='Case #%d: %d\n'%((i+1),last_tidy)
		output_list.append(output_line)
    
o = open('output_tidynumbers.txt','w')
o.writelines(output_list)
o.close()