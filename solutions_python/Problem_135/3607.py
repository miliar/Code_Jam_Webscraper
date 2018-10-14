import csv
import os

ifile = open(os.path.expanduser('~/Desktop/A-small-attempt0.in'), "rU")
reader = csv.reader(ifile)

ofile = open(os.path.expanduser('~/Desktop/problem1.out'), "wb")
writer = csv.writer(ofile)

f = open('problem1.out', 'r+')

def cardTrick():
	output = [];
	rownum = 0
	case = 0
	for row in reader:
		if (rownum == 0):
			cases = int(row[0])
			row1 = 11
			row2 = 11
		if ((rownum-1) % 10 == 0):
			row1 = int(row[0])
		if ((rownum-1) % 10 == row1):
			list1 = row[0].split()
			list1 = [int(x) for x in list1]
		if((rownum-1) % 10 == 5):
			row2 = int(row[0])
		if ((rownum-1) % 10 == 5 + row2):
			list2 = row[0].split()
			list2 = [int(x) for x in list2]
			overlap = list(set(list1) & set(list2))
			case = case + 1
			if (len(overlap) == 1):
				print("Case #" + `case` + ": " + `overlap[0]`)
				output.append(["Case #" + `case` + ": " + `overlap[0]`])
			if (len(overlap) > 1):
				print("Case #" + `case` + ": Bad magician!")
				output.append(["Case #" + `case` + ": Bad magician!"])
			if (len(overlap) == 0):
				print("Case #" + `case` + ": Volunteer cheated!")
				output.append(["Case #" + `case` + ": Volunteer cheated!"])
		rownum = rownum + 1
	print(output)
	output = "\n".join(item[0] for item in output)
	f.write(output)
	ifile.close()
	ofile.close()
	#.write("\n".join(itemlist))
	
		

cardTrick()

