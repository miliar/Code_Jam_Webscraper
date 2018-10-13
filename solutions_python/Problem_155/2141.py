f = open("A-large.in","r")
idx = -1
for l in f:
	if idx == -1 : 
		idx+=1
		continue
	idx+=1
	smax , s = l.split(' ')
	#print 'smax : '+str(smax)+' s : '+str(s)
	inv,count = 0,0
	for i in range(int(smax)+1):
		#print 'i : '+str(i)+' s : '+s[i]
		if count < i:
			inv+=(i-count)
			count+=(i-count)
		count+=int(s[i])
	print 'Case #%s: %s'%(idx,inv)
