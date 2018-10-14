

def check(num):
	num_list = list(str(num))
	flag = True
	while flag == True and len(num_list)>1:
		# print num_list
		for i in range(0,len(num_list)-1):
			if int(num_list[i]) > int(num_list[i+1]):
				num_list[i] = int(num_list[i])-1
				for j in range(i+1,len(num_list)):
					num_list[j] = 9
				flag = True
				break
			flag = False
	num_str = "".join(map(str,num_list))
	num_int = int(num_str)
	# if num_int == 0:
		# return int('9'*(len(num_list)-1))
	return num_int

# print check(1111111110)
with open('B-large.in','r') as a:
	data = a.read().split('\n')
	# print data

b = open('B.txt','w') 

for j in range(int(data.pop(0))):	
	N = int(data[j])
	b.write('Case #%d: %d\n' %(j+1,check(N))) 

