def main():
        outfile = open("Output.txt","w")
	T = int(input())
	for i in range(T):
		for p in range(2):
			rowNum = int(input())
			row1 = makeRow()
			row2 = makeRow()
			row3= makeRow()
			row4 = makeRow()
			if p == 0:
				if rowNum == 1:
					try1= row1
				elif rowNum==2:
					try1= row2
				elif rowNum == 3:
					try1= row3
				else:
					try1 = row4
			if p == 1:
				if rowNum == 1:
					try2=row1
				elif rowNum==2:
					try2=row2
				elif rowNum == 3:
					try2= row3
				else:
					try2= row4
		answers = []
		for u in try1:
			if u in try2:
				answers.append(u)				
		q = str(i+1)
		if len(answers) >1:
			outfile.write("Case #"+q+": Bad magician!")
		elif len(answers)==1:
			outfile.write("Case #"+q+":" + str(answers[0]))
		else:
			outfile.write("Case #"+q+": Volunteer cheated!")
                outfile.write("\n")
						
def makeRow():
	cards = input().split()
	return cards
main()
