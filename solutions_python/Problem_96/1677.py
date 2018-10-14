def evaluate(s,p,max_score):
	tp=p*3
	count=0
	for i in range(0,len(max_score)):
		if max_score[i]!=0:
			temp=tp-max_score[i]
			if temp<3:
				count=count+1
				continue
			if temp<5 and s>0:
				count=count+1
				s=s-1
		elif max_score[i]==0 and tp==0:
			count=count+1
	return count
f_in=open('B-large.in','r')
f_out=open('out','w')
tests=f_in.readline()
while tests!='':
	for i in range(0,int(tests)):
		num_str=f_in.readline()
		num_str=num_str.split()
		N=int(num_str[0])
		S=int(num_str[1])
		p=int(num_str[2])
		max_scores=[0]*N
		for j in range(0,N):
			max_scores[j]=int(num_str[3+j])
		count=evaluate(S,p,max_scores)
		f_out.write("Case #"+str(i+1)+": "+str(count)+"\n")
	tests=f_in.readline()
