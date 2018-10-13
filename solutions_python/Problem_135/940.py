fin=file("MagicTrickInput.txt")
fout=file("MagicTrickOutput.txt","w")
output = ""
T=int(fin.readline().strip())
for t in range(T):
	row1 = int(fin.readline().strip())
	data1 = []
	for i in range(4):
		tmp = fin.readline().strip()
		if i==row1-1:
			data1 = [x for x in tmp.split(" ")]
	row2 = int(fin.readline().strip())
	data2 = []
	for i in range(4):
		tmp = fin.readline().strip()
		if i==row2-1:
			data2 = [x for x in tmp.split(" ")]
	result = list(set(data1).intersection(set(data2)))
	l = len(result)
	if l == 0:
		output += "Case #"+str(t+1)+": Volunteer cheated!\n"
	elif l > 1:
		output += "Case #"+str(t+1)+": Bad magician!\n"
	else:
		output += "Case #"+str(t+1)+": "+str(result[0])+"\n"

fout.write(output)
fout.close()



