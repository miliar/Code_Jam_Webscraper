import os
import operator
line=1
line-=1
def reader(file_name):
	with open(file_name) as f:
		global cases
		cases=int(next(f))
		print(cases)
		for i in f:
			yield (i[:-1],)+tuple(next(f)[:-1] for i in range(line))



def solver(data):
	case=0
	A,B,K=map(int,data[0].split(' '))
	for i in range(A):
		for j in range(B):
			if(i&j<K):
				case+=1
	return case
	


input_filter=operator.methodcaller('endswith','.in')
input_files=filter(input_filter,os.listdir())
for file_name in input_files:
	case=1
	with open(file_name+'.out','w') as f:
		for data in reader(file_name):
			f.write("Case #{}: {}\n".format(case,solver(data)))
			case+=1
		
