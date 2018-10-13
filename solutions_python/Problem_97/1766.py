#!/usr/bin/env python

text_file = open("test.txt")

list_from_file=[]
list_possoble=[]

def string_shift(string, num):
	return string[-num:] + string[:-num]

for lines in text_file:
	list_from_file.append(lines.split())
	
#print list_from_file

for i, lines  in enumerate(list_from_file):
	min_num = int(lines[0])
	max_num = int(lines[1])
	list_possoble.append([])
	for numbers in xrange(min_num, max_num):
		for length in xrange(1,len(str(numbers))):
			j = int(string_shift(str(numbers),length))
			if j<=max_num and j>=min_num and j!=numbers and len(str(j))==len(str(numbers)) and [j, numbers] not in list_possoble[i] and [numbers, j] not in list_possoble[i]:
				list_possoble[i].append([numbers, j])
				
#for lines in  list_possoble[3]:
	#print lines
#remove_others(list_possoble[3])
for i, lines in enumerate(list_possoble):
	print "Case #%d:" % (i+1), len(lines)
