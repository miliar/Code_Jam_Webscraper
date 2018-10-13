x=int(input())
 
def is_tidy(num):
	num=list(str(num))
	if num[-1]=='0':
		return False
	max1=int(num[0])
	for i in range(1, len(num)):
		if int(num[i])<max1:
			return False
		max1=int(num[i])
	return True
 
for t in range(1,x+1):
	s=long(input())
	if is_tidy(s):
		print 'Case #%s: %s' % (str(t), str(s))
		continue
	arr=list(str(s))
	arr[-1]=arr[-2]
	m1=max(arr)
	if m1=='1':
		res = '9'*(len(arr)-1)
		print 'Case #%s: %s' % (str(t), str(res))
		continue
	m_index=0
	for i in range(1,len(arr)):
		if arr[m_index]<arr[i]:
			m_index=i
	arr[m_index]=str(int(arr[m_index])-1)
	for i in range(m_index+1,len(arr)):
		arr[i]='9'
	res="".join(arr)
	print 'Case #%s: %s' % (str(t), str(res))
