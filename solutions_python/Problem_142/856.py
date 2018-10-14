def judge(str1,stand):
	n = len(str1)
	kle = len(stand)
	k = 0
	last = str1[0]
	for i in range(n):
		if str1[i] != last:
		 	k += 1
		if k >= kle:
			return False
		if str1[i] != stand[k]:
		 	return False
		last = str1[i]
	
	if k != kle -1:
		return False
	
	return True

def cnt(str1):
	num = 0
	le = len(str1)
	last = str1[0]
	ans = []
	for i in range(le):
		if str1[i] == last:
			num += 1
		else:
			ans.append(num)
			num = 1
		last = str1[i]

	ans.append(num)
	return ans


case = int(raw_input())
for i in range(case):
	print "Case #%d:"%(i+1),
	flag = True
	num_str = int(raw_input())
	str_list = []
	mat = []
	
	first = raw_input()
	mat.append(cnt(first))
	stand = ""
	last = ""
	for j in range(len(first)):
		if first[j] == last :
			continue
		stand += first[j]
		last = first[j]
	#print "stamdfr",
	#print stand

	for j in range(num_str-1):
		ele = raw_input()
		mat.append(cnt(ele))
		#print "the judg strign is",
		#print ele , stand
		if judge(ele,stand) == False:
		 	print "Fegla Won"
		 	flag = False
		 	break

	if flag == False:
		continue
	#print mat
	
	sun = 0
	for j in range(len(stand)):
		sigma = []
		mid_indx = int(num_str/2)+1
		#print "here is my index",
		#print mid_indx
		for k in range(num_str):
			sigma.append(mat[k][j])
		sigma.sort()
		#print "hereh is sifma",
		#print sigma
		mid = sigma[mid_indx-1]
		#print "here is my mid",
		#print mid
		for k in range(num_str):
			sun += abs(sigma[k]-mid)
	
	print sun






