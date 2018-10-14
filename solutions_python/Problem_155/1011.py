file = open("input")

counter_i = 1
counter_end_i = file.readline()
a=[]
num=1
helper=0

def solve(a,num,helper):
	helper = 0
	it=1
	sum=0
	newhelp=0
	while(it<num):
		sum=a[it-1]+sum
		if(a[it]>0 and it > sum):
			newhelper = it-sum
			sum = sum + newhelper
			helper=helper+newhelper
		it=it+1
	return helper


while (counter_i <= int(counter_end_i.strip())):
	current_line = file.readline().strip().split(' ')
	num=1+int(current_line[0])
	a = []
	i = 0
	while (i<num):
		a.append(int(current_line[1][i]))
		i=i+1
	print "%s%d%s%d"%("Case #",counter_i,": ",solve(a,num,helper))
	counter_i=counter_i+1
