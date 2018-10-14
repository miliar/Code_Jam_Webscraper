import sys
sys.setrecursionlimit(100000)
def gcd(a,b):
	if a<b:
		c=a
		a=b
		b=c
	if b==0:
		return a
	else:
		return gcd(b,a%b)

def gcd_n(input_list,n):
	if n==1:
		return input_list[0]

	return gcd(input_list[n-1],gcd_n(input_list,n-1))






inp=raw_input()
times=int(inp)
for i in range(1,times+1):
	eachline=raw_input()
	each_split=eachline.split()
	n=int(each_split[0])
	data=[]
	for j in range(1,n):
		data.append(abs(int(each_split[j])-int(each_split[j+1])))
	
	result=gcd_n(data,n-1)
	if int(each_split[1]) % result==0:
		print 'Case #'+str(i)+': 0'
	else:
		print 'Case #'+str(i)+': '+str(result-(int(each_split[1])%result))
