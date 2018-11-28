from math import ceil,floor,log
t = int (raw_input())
for i in xrange(1,t+1):
	n, k = [int(s) for s in raw_input().split(" ")]
	# generate a dict, key is the total length of empty stalls and value is total number of them
	res_y = -1
	res_z = -1
	
	dic = {}
	dic[n] = 1
	small = int(floor((n-1)/2.0))
	large = int(ceil((n-1)/2.0))
	
	if small in dic:
		dic[small] = 1 + dic[small]
	else:
		dic[small] = 1
	
	if large in dic:
		dic[large] = 1 + dic[large]
	else:
		dic[large] = 1

	lsmall = small
	llarge = large

	while (lsmall > 0 or llarge > 0):

		if lsmall < llarge:
			x = dic[lsmall]
			y = dic[llarge]
		
			lsmall_small = int(floor((lsmall-1)/2.0))
			lsmall_large = int(ceil((lsmall-1)/2.0))
			count_lss = x
			count_lsl = x
		
			llarge_small = int(floor((llarge-1)/2.0))
			llarge_large = int(ceil((llarge-1)/2.0))
			count_lls = y
			count_lll = y

			new_lsmall = min(lsmall_small,llarge_small)
			new_llarge = max(lsmall_large,llarge_large)
		
			if new_lsmall < llarge_small:
				count_new_lsmall = x
				count_new_llarge = x + 2*y
			if new_lsmall == llarge_small:
				count_new_lsmall = 2*x + y
				count_new_llarge = y

		elif lsmall == llarge:
			lsame = lsmall
			x = dic[lsame]
			
			new_lsmall = int(floor((lsame-1)/2.0))
			new_llarge = int(ceil((lsame-1)/2.0))
			
			count_new_lsmall = x
			count_new_llarge = x
			
		if new_lsmall in dic:
			dic[new_lsmall] = count_new_lsmall + dic[new_lsmall]
		else:
			dic[new_lsmall] = count_new_lsmall
		
		if new_llarge in dic:
			dic[new_llarge] = count_new_llarge + dic[new_llarge]
		else:
			dic[new_llarge] = count_new_llarge
			
		lsmall = new_lsmall
		llarge = new_llarge
	
	itercount = 0
	for key in sorted(dic.keys(),reverse=True):
		if key > 0:
			itercount = itercount + dic[key]
			if k <= itercount:
				res_key = key
				break
	
	res_y = int(ceil((res_key-1)/2.0))
	res_z = int(floor((res_key-1)/2.0))
	#while (flag):
	#	flag = min(xmin,xmax)
	print "Case #{}: {} {}".format(i,res_y,res_z) # need to change later
