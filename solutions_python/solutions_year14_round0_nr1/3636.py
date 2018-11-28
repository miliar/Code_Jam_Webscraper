filename = "A-small-attempt4.in";
with open (filename, "r") as inputfile:
	with open ("answers.txt", "w") as outputfile: 
		data = inputfile.readlines();
		T = int(data[0]); # T test cases follow

		for i in range(len(data)):
			line = data[i];
			data[i] = line.replace('\n','');

		for ii in range(T):
			index = ii*10
			first = int(data[index + 1]) # 0, 1, 2 should map to lines 1, 11, 21
			firstArray = data[(index+2):(index+6)] # 0, 1, 2 should map to lines 2-5, 12-15, 22-25
			second = int(data[index + 6]) # 0, 1, 2 should map to lines 6, 16, 26
			secondArray = data[(index+7):(index+11)] # 0, 1, 2 should map to lines 7-10, 17-20, 27-30

			firstRow = firstArray[first-1].split(' ')
			secondRow = secondArray[second-1].split(' ')

			case = 0;
			string = "";
			for i in firstRow:
				for j in secondRow: 
					#print(i, j)
					if i == j:
						case = case + 1;
						string = ": " + str(i);
			
			if case > 1:
				case = 2;
				string = ": Bad magician!"
			if case == 0:
				case = 3;
				string = ": Volunteer cheated!"

			answer = "".join(("Case #",str(ii+1),string));
			print(answer)

			outputfile.write("".join((answer,'\n')))

readFile = open("answers.txt")
lines = readFile.readlines()
readFile.close()

w = open("answers.txt",'w')
w.writelines([item for item in lines[:-1]])
w.write(answer)
w.close()