#!/usr/bin/python

def main():
	fin = open("./data.in", "r")
	fout = open("./output.txt", "w")

	firstline = 0
	case = 0
	row = 0
	lone = []
	ltwo = []
	for line in fin:
		if firstline != 0:
		
			line = line.split()

			if len(line) == 1:
				row = int(line[0])
	
				if lone != [] and ltwo != []:
					case += 1

					fout.write("Case #" + str(case) + ": " + str(results) + "\n")
				  
					lone = []
					ltwo = []
			else:
				row -= 1
				print row
				if row == 0:

					if lone == []:
						
						lone = line
					else:
						ltwo = line
						results = Compare(lone, ltwo)

		#	print line

		firstline+= 1
	case += 1
	fout.write("Case #" + str(case) + ": " + str(results) + "\n")


def Compare(l1, l2):
	inter = list(set(l1).intersection(l2))

	if len(inter) == 1:
		return inter[0]
	elif len(inter) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"

main()

