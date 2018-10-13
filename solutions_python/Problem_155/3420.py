test_cases = int(raw_input())
i=0

while(i < test_cases):
	test_line = raw_input()
	max_shy = int(test_line.split(" ")[0])
	shyness_string = test_line.split()[1]
	shyness_array = [int(a) for a in shyness_string]
	ppl_stood = shyness_array[0]
	ppl_to_add = 0 
	j = 1
	while(j < max_shy+1):
		if(shyness_array[j] > 0 and ppl_stood < j):
			ppl_to_add += (j - ppl_stood)
			ppl_stood += ppl_to_add
		ppl_stood += shyness_array[j]
		j+=1
	print "Case #"+ str(i+1)+": "+str(ppl_to_add)
	i+=1