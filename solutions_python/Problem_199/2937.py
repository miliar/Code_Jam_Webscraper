import operator
f=open("test.txt","r")
T=f.readline()
T=int(T)

fo=open("output.txt","w")

cnt=1


def flip_subarray(lst):
	#flip 1--->-1 and -1--->1	
	
	return lst	


while T>=cnt:
	N=f.readline().replace('\n','')
	panc=N.split(' ')[0]
	k=int(N.split(' ')[1])
	#print "k",k
	num_lst=[]
	#print N,type(N),list(N)
	t_lst= list(panc)
	flip_cnt=0
	flg=0
	#print "t_lst,N   ",  t_lst,N
	for i in range(len(t_lst)):
		if t_lst[i]=='-':
			num_lst.append(0)#consider 0('-') as 1
		else:
			num_lst.append(1)#consider 1('+') as -1
	#print num_lst
	for i in range(len(num_lst)):
		#print num_lst[i]
		if num_lst[i]==0 :
			#print "i+k",i+k,len(num_lst)
			if (i+k<=len(num_lst)):
				flip_cnt+=1
				for pp in range(k):
					if num_lst[i+pp]==0:
						num_lst[i+pp]=1
					else:
						num_lst[i+pp]=0
				#print "num_lst  ",num_lst	

			else:
				#print "Impossible"
				fo.write("Case #"+str(cnt)+": "+str("IMPOSSIBLE")+"\n")
				flg=1
				break
	

	
	if flg!=1:
		#print flip_cnt
		fo.write("Case #"+str(cnt)+": "+str(flip_cnt)+"\n")


	
	# print "flip_cnt  ",flip_cnt



	
	
	#print "Case #"+str(cnt)+": "+str(flip_cnt)+"\n"
	#fo.write("Case #"+str(cnt)+": "+str(flip_cnt)+"\n")
	


	cnt+=1
f.close
fo.close()