def string_to_array(x):
    input_list = x.split()
    input_list = [float(a) for a in input_list]
    return input_list

cases = input()
j=0
answer_list=[]
while j<cases:
	n = input()
	blocks = raw_input()	
	blocks_n = string_to_array(blocks)
	blocks = raw_input()
	blocks_k = string_to_array(blocks)
	blocks_n.sort()
	blocks_k.sort()
	blocks_k_d = []
	for i in  blocks_k:
		blocks_k_d.append(i)
	blocks_n_d = []
        for i in  blocks_n:
                blocks_n_d.append(i)
	warpoints = 0
	while len(blocks_n) != 0:
		chosen_n = blocks_n[-1]
		blocks_n.pop()	
		if chosen_n > blocks_k[-1]:
			chosen_k = blocks_k[0]
			blocks_k.pop(0)
			warpoints +=1
		else:
			chosen_k = blocks_k[-1]
			blocks_k.pop()
		
	d_warpoints=0
	blocks_k_d.sort()
	blocks_n_d.sort()
	while len(blocks_n_d) !=0:
		
		if blocks_n_d[-1] > blocks_k_d[-1]:
			chosen_k = blocks_k_d[0]
			blocks_k_d.pop(0)
			for i in blocks_n_d:
				if i - chosen_k >0:
					chosen_n = i
					blocks_n_d.pop(blocks_n_d.index(i))
					d_warpoints +=1

					break
		else:
			chosen_n = blocks_n_d[0]
			chosen_k = blocks_n_d[-1]
			blocks_n_d.pop(0)
			blocks_k_d.pop(-1)
	j+=1
	answer_list.append([d_warpoints,warpoints])

i=0
while i<cases:
    print "Case #"+str(i+1)+": "+str(answer_list[i][0])+" "+str(answer_list[i][1])
    i+=1

