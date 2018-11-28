import os

input = "A-large.in"
output = input + "-result.txt"

i_file = open(input,'r')
o_file = open(output,'w')

testcases = int(i_file.readline())

for i in range(1,testcases+1):
	line = i_file.readline()
	numbers = line.split()
	
	max_shyness = int(numbers[0])
	people = numbers[1]
	
	total_people = 0
	bring_friend = 0
	
	
	for j in range(max_shyness+1):
		cur_shyness = j
		people_in_need = int(people[j])
		bring_friend_here = 0
		
		if total_people < cur_shyness:
			bring_friend_here = cur_shyness	- total_people		
			bring_friend += bring_friend_here
			
		total_people += bring_friend_here + people_in_need
		
	print "Case #",i,": ", bring_friend
	o_file.write("Case #")
	o_file.write(str(i))
	o_file.write(": ")
	o_file.write(str(bring_friend))
	o_file.write('\n')
	

i_file.close()
o_file.close()
	


