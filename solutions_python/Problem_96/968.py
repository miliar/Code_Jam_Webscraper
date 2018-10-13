Python 2.7.2 (default, Jun 12 2011, 14:24:46) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fp=open('B-large.in')
>>> ot=open('out.txt','w')
>>> for idx in range(int(fp.readline())):
	arr=[int(n) for n in fp.readline().split()]
	cnt=arr[0]
	sup=arr[1]
	mx=arr[2]
	gog=arr[3:3+arr[0]]
	gog_cnt=0
	for val in gog:
		temp=val-mx
		if temp>=0:
			temp=temp/2
			diff=mx-int(temp)
			if diff ==2 and sup>0:
				gog_cnt=gog_cnt+1
				sup=sup-1
			elif diff<2:
				gog_cnt=gog_cnt+1
	ot.write('Case #%d: %d\n'%(idx+1,gog_cnt))

	
>>> ot.close()
>>> 
