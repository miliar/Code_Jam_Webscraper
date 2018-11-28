# !/usr/bin/python2.7
# -*- coding:utf-8 -*-

# By: Vasanthi Vuppuluri
# Last modified date: April 11, 2014

import os

def main():
	T = raw_input() # Number of test cases
	T = int(T)
	if (1 <= T <= 100):
		
		i = 0
		
		
		global Output
		Output = []		
		
		for case in xrange(0, T):
			
			fn = raw_input() # row number selected from first arrangement
			fn = int(fn)
			
			
			if (1 <= fn <= 4):
				row_1 = raw_input()
				row_1 = row_1.split()
				row1 = []
				if (len(row_1) == 4) and (len(row_1) == len(set(row_1))):
					for i in row_1:
							i = int(i)
							row1.append(i)
				
				row_2 = raw_input()
				row_2 = row_2.split()
				row2 = []
				if (len(row_2) == 4) and (len(row_2) == len(set(row_2))):
					for i in row_2:
						i = int(i)
						row2.append(i)
				
				row_3 = raw_input()
				row_3 = row_3.split()
				row3 = []
				if (len(row_3) == 4) and (len(row_3) == len(set(row_3))):
					for i in row_3:
						i = int(i)
						row3.append(i)
				
				row_4 = raw_input()
				row_4 = row_4.split()
				row4 = []
				if (len(row_4) == 4) and (len(row_4) == len(set(row_4))):
					for i in row_4:
						i = int(i)
						row4.append(i)
				
				if ((set(row_1) & set(row_2)) or (set(row_1) & set(row_3)) or (set(row_1) & set(row_4)) or (set(row_2) & set(row_3)) or (set(row_2) & set(row_4)) or (set(row_3) & set(row_4))):
					break

			# Storing the row values of the selected row
			list_1 = []

			if (int(fn) == 1):
				list_1 = row1
			
			elif (int(fn) == 2):
				list_1 = row2
			
			elif (int(fn) == 3):
				list_1 = row3
			
			elif (int(fn) == 4):
				list_1 = row4
			
					
			# Second row number and arrangement
			sn = raw_input() # row number selected from second arrangement
			sn = int(sn)
			
			if (1 <= sn <= 4):
				row_1 = raw_input()
				row_1 = row_1.split()
				row1 = []
				if (len(row_1) == 4) and (len(row_1) == len(set(row_1))):
					for i in row_1:
							i = int(i)
							row1.append(i)
				
				row_2 = raw_input()
				row_2 = row_2.split()
				row2 = []
				if (len(row_2) == 4) and (len(row_2) == len(set(row_2))):
					for i in row_2:
						i = int(i)
						row2.append(i)
				
				row_3 = raw_input()
				row_3 = row_3.split()
				row3 = []
				if (len(row_3) == 4) and (len(row_3) == len(set(row_3))):
					for i in row_3:
						i = int(i)
						row3.append(i)
				
				row_4 = raw_input()
				row_4 = row_4.split()
				row4 = []
				if (len(row_4) == 4) and (len(row_4) == len(set(row_4))):
					for i in row_4:
						i = int(i)
						row4.append(i)
				
				if ((set(row_1) & set(row_2)) or (set(row_1) & set(row_3)) or (set(row_1) & set(row_4)) or (set(row_2) & set(row_3)) or (set(row_2) & set(row_4)) or (set(row_3) & set(row_4))):
					break

			# Storing the row values of the selected row
			list_2 = []

			if (int(sn) == 1):
				list_2 = row1
			
			elif (int(sn) == 2):
				list_2 = row2
			
			elif (int(sn) == 3):
				list_2 = row3
			
			elif (int(sn) == 4):
				list_2 = row4
			
			
			# Comparing list_1 and list_2
			
			imagined_numbers = 0

			if(set(list_1) & set(list_2)):
				list_3 = []
				list_3 = set(list_2) & set(list_1)
				imagined_numbers = len(list_3)

			# Output
		
			if (imagined_numbers == 1):
				for number in list_3:
					number = int(number)
					op = "Case #%d: %d" %(case+1,number)
					Output.append(op)

			elif (imagined_numbers < 1):
				op = "Case #%d: %s" %(case+1, 'Volunteer cheated!')
				Output.append(op)

			elif (imagined_numbers > 1):
				op = "Case #%d: %s" %(case+1, 'Bad magician!')
				Output.append(op)

		ofile = 'Output.txt'
		if os.path.isfile(ofile):
			os.remove(ofile)
		
		ofile = open(ofile,'a')
		
		for op in Output:
			ofile.write(op)
			ofile.write('\n')

		ofile.close()

if __name__ == "__main__":
    main()