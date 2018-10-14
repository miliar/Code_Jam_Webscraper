def main():
	file = open('input.txt')
	output = open('output.txt', 'w')
	cases = file.readline().replace("\n", "")
	for n in range(0, int(cases)):
		line = int(file.readline().replace("\n", ""))
		i=1
		while(i<line):
			file.readline()
			i = i+1

		list1 = file.readline().split()
		i=i+1

		while(i<=4):
			file.readline()
			i = i+1

		line = int(file.readline()[0:1])

		i=1
		while(i<line):
			file.readline()
			i = i+1

		list2 = file.readline().split()
		i=i+1

		while(i<=4):
			file.readline()
			i = i+1
		finallist = list(set(list1) & set(list2))

		if len(finallist)>1:
			output.write("Case #"+str(n+1)+": Bad magician!\n")
		elif len(finallist)<1:
			output.write("Case #"+str(n+1)+": Volunteer cheated!\n")
		else:
			output.write("Case #"+str(n+1)+": "+finallist[0]+"\n")


	file.close()
	output.close()

main()
