import sys
import os
import re
os.system('clear')


def main():
	testcases =input()
	for case in range(0,testcases):
		
		first_matrix = []
		first_choice = input()
		for i in range(0,4):
			row_input =raw_input()
			row = row_input.split(' ')
			first_matrix.append(row)
			i+=1
		#print first_matrix

		first_answer = first_matrix[first_choice-1]
		#print first_answer

		second_matrix = []
		second_choice = input()
		for i in range(0,4):
			row_input =raw_input()
			row = row_input.split(' ')
			second_matrix.append(row)
			i+=1
		#print second_matrix

		second_answer = second_matrix[second_choice-1]
		#print second_answer
		
		counter =0
		for element in first_answer:
			if element in second_answer:
				answer = element
				counter +=1
		#print counter
		cases=case+1
			
		if counter == 0:
			print 'Case #'+ str(cases) + ': Volunteer cheated!'
		
		elif counter == 1:
			print 'Case #'+ str(cases) + ': ' +str(answer)
		else:
			print 'Case #'+ str(cases) + ': Bad magician!'

		case +=1

if __name__ == "__main__":
	main()
