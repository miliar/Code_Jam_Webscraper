fil = open('1.txt','r+')
data = fil.readlines()
fil.close()
out = open('out.txt','a+')
cases = int(data[0].strip())
def match(arr1,arr2):
	re = list(set(arr1).intersection(arr2))
	if len(re) == 1:
		return str(re[0])
	elif len(re) >1 :
		return "Bad magician!"
	elif len(re) == 0:
		return "Volunteer cheated!"
for i in range(0,cases):
	q1 = int(data[10*i+1].strip())
	array1 = data[10*i+1+q1].strip().split()
	q2 = int(data[10*i+6].strip())
	array2 = data[10*i+6+q2].strip().split()
	val = match(array1,array2)
	out.writelines("case #"+str(i+1)+": "+val+"\n")
out.close()