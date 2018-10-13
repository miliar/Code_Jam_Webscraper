reader = open("A-large.in")
writer = open("A-large.out", "w") #writer.write(string + "\n")

def flip(value, start, length):
	if(len(value)<start+length):
		return value, False
	for i in range(start, start+length):
		if(value[i:i+1]=="+"):
			value = value[0:i] + "-" + value[i+1:len(value)]
		else:
			value = value[0:i] + "+" + value[i+1:len(value)]
	return value, True

def run(value,tool):
	ctr=0 
	for i in range(0, len(value)):
		if(value[i:i+1]=="-"):
			ctr+=1
			res = flip(value,i,tool)
			value = res[0]
			if(res[1] == False):
				return -1,False
	return ctr, True

N = int(reader.readline())
print(N)
for itr in range(0,N):
	current = reader.readline()
	if(itr<N):
		current = current[0:len(current)-1]
	cur = current.split(" ")
	#print("Case #"+str(itr+1)+": "+current)

	res = run(cur[0],int(cur[1]))

	if(res[1]==True):
		print("Case #"+str(itr+1)+": "+str(res[0]))
		writer.write("Case #"+str(itr+1)+": "+str(res[0])+"\n")
	else:
		print("Case #"+str(itr+1)+": "+"IMPOSSIBLE")
		writer.write("Case #"+str(itr+1)+": "+"IMPOSSIBLE"+"\n")