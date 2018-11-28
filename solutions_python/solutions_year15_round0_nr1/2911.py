#!/usr/bin/python

T = input()
input_lines = []
s_max = []
s_value_string = []
s_values = []
output = []

for i in range(0,T):
	s_max.append(0)
	s_value_string.append(0)
	input_lines.append(raw_input())


for i in range(0,T):
	s_max[i],s_value_string[i] = input_lines[i].split() 
	s_values.append(list(str(s_value_string[i])))
	

for i in range(0,T):
	count = 0
	standing = 0
	for j in range(0,int(s_max[i])+1):
		if (j==0):
			if (int(s_values[i][j])==0):
				count += 1
				standing +=1
			else:
				standing += int(s_values[i][j])
		else:
			if (standing<j and int(s_values[i][j])!=0):
				count += (j-standing)
				standing += (j-standing)
				standing += int(s_values[i][j])	
			else:
				standing += int(s_values[i][j])	
	output.append(count)

for i in range(0,T):
	print "Case #"+str(i+1)+": "+str(output[i])





		 






#for i in range(0,T):
#	print s_max[i]
#	print s_value_string[i]
#	print s_values[i]
	

#print s_values
#print s_values[1][0]

