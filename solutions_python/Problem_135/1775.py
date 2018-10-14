with open("A-small-attempt2.in") as f:
	raw_data=f.read()
raw_data=raw_data.split("\n")
for i in range(len(raw_data)):
	try:
		raw_data[i]=int(raw_data[i])
	except:
		raw_data[i]=list(map(int,filter(bool,raw_data[i].split(" "))))
outputs=[]
data=[]
for i in range(raw_data[0]):
	datum=[]
	print(i*10+2)
	datum.append(raw_data[i*10+1])
	datum.append(raw_data[i*10+2:i*10+6])
	datum.append(raw_data[i*10+6])
	datum.append(raw_data[i*10+7:i*10+11])
	data.append(datum)
	print(datum)
with open("output","w") as f:
	for index,i in enumerate(data):
		set1=set(i[1][i[0]-1])
		set2=set(i[3][i[2]-1])
		difference=set1.intersection(set2)
		if not difference:
			f.write("Case #{}: Volunteer cheated!\n".format(index+1))
		elif len(difference)==1:
			f.write("Case #{}: {}\n".format(index+1,list(difference)[0]))
		else:
			f.write("Case #{}: Bad magician!\n".format(index+1))
