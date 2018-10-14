def numshift(s,p):
	#print s
	#print 'is shifted by '+str(p)
	strn=''
	for i in range(p,len(s)):
		strn = strn+s[i]
	#print str
	for i in range(0,p):
		strn = strn+s[i]
	#print strn
	return int(strn)
	
def shift(s,count):
	#print s
	#print 'shifting by '+str(count)
	start = count
	flag = 0
	while start<len(dig) and flag==0:
		#print 'comparing '+str(dig[start])+'with '+str(dig[start-count])
		if dig[start]>dig[start-count]:
			flag = 1;
		else:
			start=start+1;
	if flag==0:
		last = start-count
		start = 0
		while start<count and flag==0:
			#print 'comparing '+str(dig[start])+'with '+str(dig[last])
			if dig[start]>dig[last]:
				flag = 1;
			else:
				start=start+1;
				last=last+1;
	return flag

testcase = None
while not testcase:
    try:
        testcase = int(raw_input())
    except ValueError:
        print 'Invalid testcase'
#print 'testcase is '+str(testcase)
for imn in range(testcase):
	biglist=[]
	s = raw_input();
	s_list = s.split(' ');
	low = int(s_list[0]);
	high = int(s_list[1]);
	succount = 0
	for input in range(low,high+1):
		s = str(input);
		length = len(s);
		dig=[]
		for i in range(length):
			dig.append(int(s[i]))
		#print 'input is '+s+' len is '+str(length)
		if len(dig)==1:
			succount = 0
		else:
			for j in range(len(dig)-1):
				#print 'j is '+str(j)
				num = numshift(s,j+1);
				#print s+' is shifted by '+str(j+1)+' to '+str(num)
				if num<=high and num>=low and num>int(s):
					tstr = s+'.'+str(num)
					if tstr not in biglist:
						biglist.append(s+'.'+str(num))
						succount=succount+1
	print 'Case #'+str(imn+1)+': '+ str(succount)