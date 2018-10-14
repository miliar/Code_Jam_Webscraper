file = open('/users/ahn/desktop/input.txt')
input = file.read()
file.close()

T = int(input.split('\n')[0])

N=[]
data=[]
for i in range(0,T):
	data += [[]]

for i in range(0,T):
	N += [int(input.split('\n')[2*i+1])]
	data[i] += input.split('\n')[2*i+2].split(' ')
	
for i in range(0,len(data)):
	for j in range(0,len(data[i])):
		data[i][j] = int(data[i][j])

def binary_add(a,b):
	result = 0
	for i in range(0,21):
		if (a%pow(2,i+1))/pow(2,i) + (b%pow(2,i+1))/pow(2,i) == 1:
			result += pow(2,i)
	return result

avail=[]
max=[]
for i in range(0,T):
	sum=0
	max_sum=0
	min = pow(10,6)+1
	for j in range(0,N[i]):
		sum = binary_add(sum,data[i][j])
		max_sum+=data[i][j]
		if data[i][j] < min:
			min = data[i][j]
	max+=[max_sum-min]
	if sum is 0:
		avail += [True]
	else:
		avail += [False]

out=''
for i in range(0,T):
	out+='Case #'+str(i+1)+': '
	if avail[i]:
		out+=str(max[i])+'\n'
	else:
		out+='NO\n'
		
file=open('/users/ahn/desktop/output.txt','w')
file.write(out)
file.close()