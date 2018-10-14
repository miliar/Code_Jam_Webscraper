import sys

def main():

	filename = ""

	for arg in sys.argv:
		filename = arg
		print arg

	ins = open( filename, "r" )
	array = []
	ins.close

	for line in ins:
		newstr = line.replace("\n", "")
		array.append(newstr)

	record = int(array[0])


	for x in range(0 , record):
		user_input1_row = int(array[(x*10)+1])
		user_input2_row = int(array[(x*10)+6])
		row1 = array[(x*10)+1+user_input1_row]
		row1 = row1.split(" ")
		row2 = array[(x*10)+6+user_input2_row]
		row2 = row2.split(" ")

		overlap = []
		for y in row1:
			for z in row2:
				if y == z:
					overlap.append(y)
		overlap_count = len(overlap)
		with open("result.txt", "a") as myfile:

			if overlap_count == 0:
				print "Case #"+ str(x+1) +": Volunteer cheated!"
				myfile.write("Case #"+ str(x+1) +": Volunteer cheated!\n")
			elif overlap_count == 1:
				print "Case #"+ str(x+1) +": "+ str(overlap[0])
				myfile.write("Case #"+ str(x+1) +": "+ str(overlap[0])+"\n")
			elif overlap_count > 1:
				print "Case #"+ str(x+1) +": Bad magician!"
				myfile.write("Case #"+ str(x+1) +": Bad magician!\n")
		myfile.close

if __name__ == "__main__":
	main()