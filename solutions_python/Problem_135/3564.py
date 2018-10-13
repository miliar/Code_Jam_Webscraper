
def find_multiples(array1,array2):
	out = []
	for e1 in array1:
		for e2 in array2:
			if e1==e2:
				out.append(e1)
	return out
		


f = open("problem1.in")
w = open("problem1_out.txt",'w')

num_samples = int(f.readline())
count = 0
row = 0

while count < num_samples:
	row1 = int(f.readline())
	for i in range(1,5):
		r1 = f.readline()
		if i == row1:
			row1_of_array = r1.strip().split(" ")
	#print row1_of_array
	
	row2 = int(f.readline())
	for i in range(1,5):
		r2 = f.readline()
		if i == row2:
			row2_of_array = r2.strip().split(" ")
	#print row2_of_array
	
	solution = find_multiples(row1_of_array,row2_of_array)
	count += 1
	
	string = ""
	
	if len(solution) == 0:
		string = "Volunteer cheated!"
	elif len(solution) == 1:
		string = solution[0]
	else:
		string = "Bad magician!"
	
	w.write("Case #"+str(count)+": " + string+'\n')



f.close()
w.close()
