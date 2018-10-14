#! /usr/bin/env python3
quaterion_table = {1:1
	,'i':2
	,'j':3
	,'k':4
	,'-i':-2
	,'-j':-3
	,'-k':-4
}
file_read = open("3a.in","r")
file_write = open("3a.out","w+")
def checkRepeat(x):
	if((len(x)*x[0]) == x):
		return True
	else:
		return False
def matrixTableGeneration(a,b):
	sign = 1
	if((a * b)<0):
		sign =-1
	if(a != -1):
		a=abs(a)
	if(b != -1):
		b = abs(b)
	if((a == 2) & (b==3)):
		return (sign * 4)
	if((a == 2) & (b == 4)):
		return (sign * -3)
	if((a == 3) & (b == 2)):
		return (sign * -4)
	if((a == 3) & (b == 4)):
		return (sign * 2)
	if((a == 4) & (b == 2)):
		return (sign * 3)
	if((a == 4) & (b == 3)):
		return (sign * -2)
	if((a == b)):
		return (sign * -1)
	if(a == (-1)):
		return (b * -1)
	if(b == (-1)):
		return (a * -1)
	if(a == 1):
		return b
	if(b == 1):
		return a
num_cases = int(file_read.readline().strip())
for case_id in range(1,num_cases+1):
	length_of_string,repetition_factor = (file_read.readline()).split()
	length_of_string = int(length_of_string)
	flag = 0
	pattern = file_read.readline()[:-1:]
	repetition_factor = int(repetition_factor)
	repeated_pattern = pattern*repetition_factor
	quaternion = list(x for x in repeated_pattern)
	quaternion = list(quaterion_table[x] for x in quaternion)
	if((len(repeated_pattern) < 3)|(checkRepeat(repeated_pattern))):
		file_write.write("Case #%d: %s\n"%(case_id,"NO"))
		continue
	if((quaternion[0] == 2)&(quaternion[1] == 3)&(quaternion[2] == 4)&(len(quaternion) == 3)):
		file_write.write("Case #%d: %s\n"%(case_id,"YES"))
		continue
	else:
		while(((quaternion[0] != 2)|(quaternion[1] != 3)|(quaternion[2] != 4))|(flag == 0)):
			if(len(quaternion) == 3):
				file_write.write("Case #%d: %s\n"%(case_id,"NO"))
				flag=1
				break
			else:
				if(len(quaternion) < 3):
					file_write.write("Case #%d: %s\n"%(case_id,"NO"))
					break
				while(quaternion[0] != 2):
					first_char = quaternion[0]
					second_char = quaternion[1]
					product = matrixTableGeneration(first_char,second_char)
					quaternion = quaternion[1::]
					quaternion[0] = product
					if(quaternion[0] == 2):
						break
					if(len(quaternion) <= 3):
						flag=1
						break
				if(len(quaternion) < 3):
					file_write.write("Case #%d: %s\n"%(case_id,"NO"))
					break
				while(quaternion[1] != 3):
					first_char = quaternion[1]
					second_char = quaternion[2]
					product = matrixTableGeneration(first_char,second_char)
					quaternion = [quaternion[0]]+quaternion[2::]
					quaternion[1] = product
					if(quaternion[1] == 3):
						break
					if(len(quaternion) <= 3):
						flag = 1
						break
				if(len(quaternion) < 3):
					file_write.write("Case #%d: %s\n"%(case_id,"NO"))
					break
				while(len(quaternion) > 3):
					first_char = quaternion[2]
					second_char = quaternion[3]
					product = matrixTableGeneration(first_char,second_char)
					quaternion = [quaternion[0]]+[quaternion[1]]+quaternion[3::]
					quaternion[2] = product
					if((quaternion[2] == 4)&(len(quaternion) == 3)):
						break
					if(len(quaternion) <= 3):
						flag=1
						break
				if(len(quaternion) == 3):
					if((quaternion[0] == 2)&(quaternion[1] == 3)&(quaternion[2] == 4)):
						file_write.write("Case #%d: %s\n"%(case_id,"Yes"))
						break
file_read.close()
file_write.close()