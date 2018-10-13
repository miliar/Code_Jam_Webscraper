import copy
inf=open('B-small-attempt4.in','r')
outf=open('small2.out','w')
count_case=int(inf.readline())
def opt(num_l):
	
	num_l.sort(reverse=True)
	#print (num_l)
	tmp=num_l[0]
	if tmp<=3:
		return tmp
	tri_num_l=copy.deepcopy(num_l)
	num_l[0]=tmp-int(tmp/2)
	num_l.append(int(tmp/2))
	tri_num_l[0]=tmp-int(tmp/3)
	tri_num_l.append(int(tmp/3))
	nopt=min(opt(num_l)+1,opt(tri_num_l)+1)

	#print(tmp)
	if tmp<=nopt:
		return tmp
	else:
		return nopt
	

for i in range(count_case):
	have=int(inf.readline())
	num_o=inf.readline().split()
	num_l=[]
	for o in num_o:
		num_l.append(int(o))
	result=opt(num_l)
	#print(result)


	# change=True
	# count=0
	# m=0
	# ind=False
	# while change:
	# 	num_l.sort(reverse=True)
	# 	m=num_l[0]
	# 	#print(num_l)
	# 	change=False
	# 	l=len(num_l)
	# 	tmp_count=0
	# 	#tmp_num=copy.deepcopy(num_l)
	# 	for j in range(l):
	# 		tmp=tmp_num[j]
	# 		if tmp>3:
	# 			# num_l[j]=tmp-int(tmp/2)
	# 			# num_l.append(int(tmp/2))
	# 			# if change==False:
	# 			# 	change=True
	# 			tmp_count+=1
	# 			#print(num_l)
	# 		else:
	# 			break
	# 	if m<tmp_count+max(num_l):
	# 		count+=m
	# 		ind=True
	# 		break
	# 	else:
	# 		count+=tmp_count

	# if not ind:	
	# 	count+=max(num_l)
	#print(count)
	#print('\n')				

	outf.write("Case #"+str(i+1)+": "+str(result)+'\n')
inf.close()
outf.close()


