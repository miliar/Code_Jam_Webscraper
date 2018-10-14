inn = open('in','r')
f = open('out','w')
n = int(inn.readline().strip())
for case in range(n):
	total_sum = 0
	to_add = 0
	s = [int(x) for x in inn.readline().split()[1].strip()]
	for i in range(len(s)):
		if s[i]>0 and i>total_sum:
			to_add+=i-total_sum
                        total_sum+=to_add
		total_sum+=s[i]

	w = "Case #"+str(case+1)+": "+str(to_add)
	print w
        f.write(w+'\n')

inn.close()
f.close()

	

 
