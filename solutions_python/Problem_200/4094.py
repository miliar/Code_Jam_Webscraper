def break_point(s):
	cur=s[0]
	cur_index=0
	for i in range(len(s)):
		if cur>s[i]:
			return cur_index
		cur=s[i]
		cur_index=i
	return -1
def where_to_decrease(s,index):
	i=index
	while i>=0:
		if s[i]!=s[index]:	return i+1
		i-=1
	return i+1
def make_number(s,index):
	s[index]-=1
	for i in range(index+1,len(s)):
		s[i]=9

tc=int(input())
for x in range(tc):
	s=list(input())
	s=[int(x) for x in s]
	print('Case #%d: '%(x+1),end='')
	ans=''
	if break_point(s)!=-1:
		make_number(s,where_to_decrease(s,break_point(s)))
		ans=''.join(str(x) for x in s)
	else:
		ans=''.join(str(x) for x in s)

	print(ans.strip('0'))

