def convert_to_array(x):
    lst = x.split()
    lst = [float(a) for a in lst]
    return lst

total = input()
j=0
answer_list=[]
while j<total:
	n = input()
	blocks = raw_input()	
	naomi = convert_to_array(blocks)
	blocks = raw_input()
	ken = convert_to_array(blocks)
	naomi.sort()
	ken.sort()
	naomi_dec = []
        for i in  naomi:
                naomi_dec.append(i)

	ken_dec = []
	for i in  ken:
		ken_dec.append(i)
	warpoints = 0
	while len(naomi) != 0:
		chosen_n = naomi[-1]
		naomi.pop()	
		if chosen_n > ken[-1]:
			chosen_k = ken[0]
			ken.pop(0)
			warpoints +=1
		else:
			chosen_k = ken[-1]
			ken.pop()
	dec_warpoints=0
	ken_dec.sort()
	naomi_dec.sort()
	while len(naomi_dec) !=0:
	
		if naomi_dec[-1] < ken_dec[-1]:
			chosen_n = naomi_dec[0]
			chosen_k = naomi_dec[-1]
			naomi_dec.pop(0)
			ken_dec.pop(-1)		
		else:
			chosen_k = ken_dec[0]
			ken_dec.pop(0)
			for i in naomi_dec:
				if i - chosen_k >0:
					chosen_n = i
					naomi_dec.pop(naomi_dec.index(i))
					dec_warpoints +=1
					break

	j+=1
	answer_list.append([dec_warpoints,warpoints])

i=0
while i<total:
    print "Case"+" #"+str(i+1)+": "+str(answer_list[i][0])+" "+str(answer_list[i][1])
    i+=1

