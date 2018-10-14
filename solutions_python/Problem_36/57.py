global count
N= int(raw_input())
for i in range(1,N+1):
	print 'Case #%d:'%i,
	mstr= raw_input()
	mstr_len=len(mstr)
	count=0
	array=[]
	pattern="welcome to code jam"
	pattern_len=len(pattern)
	array.append([1]*mstr_len)
	for j in range(pattern_len):
		array.append([0]*mstr_len)
		if j==0 and mstr[0]==pattern[0]:
			array[1][0]=1
		for k in range(1,mstr_len):
			array[j+1][k]=(array[j+1][k-1]+(mstr[k]==pattern[j] and array[j][k-1] or 0))%10000
	print "%04d"%array[pattern_len][mstr_len-1]