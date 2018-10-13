#for small datasets only

import math 

number_of_testcases = 0
listofranges = []

min_num = 99999999
max_num = -1

class pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second

def isPalindrome(numberString):
	numberString = str(numberString)
	reversedString = ''.join(reversed(numberString))
	if reversedString == numberString:
		return True
	else:
		return False

filename = "smallinput.txt"
lines = [line.strip() for line in  open(filename)]
number_of_testcases = int(lines[0])
lines.remove(lines[0])

for line in lines: 
	#print line
	if min_num > int(line.split(" ")[0]):
		min_num = int(line.split(" ")[0])
	if max_num < int(line.split(" ")[1]):
		max_num = int(line.split(" ")[1])
	
	listofranges.append(pair(int(line.split(" ")[0]), int(line.split(" ")[1])))

pq_list = []

for num in range(min_num, max_num + 1):
	if (int(math.sqrt(num)) * int(math.sqrt(num))) == int(num):

		#however, remove is the number is not a palindrome
		a = num
		b = int(math.sqrt(num))
		if isPalindrome(a) and isPalindrome(b):
			pq_list.append(num)
		
case_number = 1
#print pq_list

for item in listofranges:
	count = 0
	#for number in range(item.first, item.second + 1):
	
	for pos_num in pq_list:
		if pos_num >= item.first and pos_num <= item.second:
			count += 1

	print "Case #"+ str(case_number)+": "+str(count)
	case_number += 1
