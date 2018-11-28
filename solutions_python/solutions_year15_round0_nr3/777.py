import os

table = {}
			
table[ ('1','1') ] = '1'
table[ ('1','i') ] = 'i'
table[ ('1','j') ] = 'j'
table[ ('1','k') ] = 'k'
table[ ('i','1') ] = 'i'
table[ ('i','i') ] = '-1'
table[ ('i','j') ] = 'k'
table[ ('i','k') ] = '-j'
table[ ('j','1') ] = 'j'
table[ ('j','i') ] = '-k'
table[ ('j','j') ] = '-1'
table[ ('j','k') ] = 'i'
table[ ('k','1') ] = 'k'
table[ ('k','i') ] = 'j'
table[ ('k','j') ] = '-i'
table[ ('k','k') ] = '-1'

def use_table(avalue, bvalue, negs):
	result_value = table[ (avalue, bvalue) ]
	if negs%2==1:
		if result_value[0]=='-':
			result_value=result_value[1:]
		else:
			result_value= '-' + result_value
			
	return result_value

def actual_value(a_string):	
	a_value  = '1'
	for i in a_string:
		if a_value[0]=='-':		
			a_value=use_table(a_value[1:],i,1)
		else:
			a_value=use_table(a_value,i,0)
			
	return a_value

def simplify(a_string):	
	if len(a_string) < 5:
		return a_string
	simplified = False
	for i in range(len(a_string)-4):
		if a_string[i:i+5] == 'iiiii':
			simplified = True
			a_string = a_string[:i]+'i'+a_string[i+5:]
		elif a_string[i:i+5] == 'jjjjj':
			simplified = True
			a_string = a_string[:i]+'j'+a_string[i+5:]
		elif a_string[i:i+5] == 'kkkkk':
			simplified = True
			a_string = a_string[:i]+'k'+a_string[i+5:]
			
	if simplified:
		return simplify(a_string)
	return a_string
	

#input = "prueba.txt"
input = "C-small-attempt1.in"
output = input + "-result.txt"

i_file = open(input,'r')
o_file = open(output,'w')

testcases = int(i_file.readline())

for i in range(1,testcases+1):

	nums = i_file.readline().split()
	ijkstring = (i_file.readline())[:-1]
	veredict = ""

	fullstring = simplify(ijkstring * int(nums[1]))
	if len(fullstring)<3:
		veredict="NO"
	else:
		veredict = 'NO'
		if actual_value(fullstring) == '-1':
			for isize in range(1,len(fullstring)-1):
			
				flag_i = False
				
				if actual_value(simplify(fullstring[0:isize])) == 'i':
					for jsize in range(isize+1, len(fullstring)):
						#print isize,jsize
						flag_j = False
						if actual_value( simplify(fullstring[isize: jsize])) == 'j' and actual_value(simplify(fullstring[jsize:] )):
								veredict = "YES"
								flag_i = True
								break
					
								
				if flag_i:
					break
		else:
			veredict = 'NO'
			
		"""veredict="NO"
		for isize in range(1,len(fullstring)-1):
			
			flag_i = False
			
			if actual_value(simplify(fullstring[0:isize])) == 'i':
				for jsize in range(isize+1, len(fullstring)):
					#print isize,jsize
					flag_j = False
					if actual_value( simplify(fullstring[isize: jsize])) == 'j' and actual_value(simplify(fullstring[jsize:] )):
							veredict = "YES"
							flag_i = True
							break
				
							
			if flag_i:
				break
			"""			
		
	print "Case #",i,": " ,veredict
	#raw_input()
	
	o_file.write("Case #")
	o_file.write(str(i))
	o_file.write(": ")
	o_file.write(veredict)
	o_file.write('\n')
	
	

i_file.close()
o_file.close()