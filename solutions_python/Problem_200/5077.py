n=int(raw_input())
j=1
for j in range(1,n+1):
 num =int(raw_input())

 for i in range(num,0,-1):
	num_str = str(i)
	i_list = list(num_str)
	if(all(i_list[i] <= i_list[i+1] for i in xrange(len(i_list)-1))):
		print("Case #%d: %r"%(j,i))
		break
	else:
		i=i-1
j=j+1
	
	
	