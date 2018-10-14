from sys import stdin,stdout
from math import log,floor
t = int(stdin.readline())
for tc in range(t):
	n,k = map(int,stdin.readline().strip().split())
	levels = int(floor(log(k,2)))
	remaining = k - 2**levels
	left_num = 0
	left_num_count = 0
	
	right_num = 0
	right_num_count = 0
	left_num = n
	left_num_count = 1
	
	temp_n = n
	for i in range(levels):
		if temp_n%2 != 0:
			left_num_count = left_num_count*2 + right_num_count
			right_num_count = right_num_count
		if(temp_n%2==0):
			right_num_count = 2**(i+1) - left_num_count
			
		temp_n = temp_n/2
		
	
	num = n / 2**levels
	#print "left_count",left_num_count,"reaming",remaining,"num",num

	if num%2==0:
		if remaining < left_num_count:
			max_lr = num/2
			min_lr = max(max_lr - 1,0)
		else:
			min_lr = (num -1)/2
			max_lr = min_lr
	else:
		if remaining < left_num_count:
			max_lr = num/2
			min_lr = max_lr
		else:
			max_lr = num/2
			min_lr = max(0,max_lr - 1)
	print "Case #{}: {} {}".format(tc+1,max_lr,min_lr)
	