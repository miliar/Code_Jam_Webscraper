with open(input()) as f:
	raw_data=f.read().split("\n")
	if raw_data[-1]:
		index=None
	else:
		index=-1
data=[]
for i in raw_data[1:index]:
	data.append(list(map(float,i.split(" "))))
with open("output","w") as output:
	for index,item in enumerate(data):
		C=item[0]
		F=item[1]
		X=item[2]
		S=1
		old_time=X/2
		new_time=X/(2+F)+C/2
		while new_time<old_time:
			S+=1
			old_time=new_time
			new_time=X/(2+F*S)
			adder=0
			for i in range(0,S):
				adder+=1/(2+F*i)
			new_time+=adder*C
		output.write("Case #{}: {}\n".format(index+1,old_time))
