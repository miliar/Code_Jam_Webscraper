import os

data_filename = 'A-small-attempt0.in'
output_filename = 'A-small-attempt0.out'

file_in = open(data_filename, 'r')
read_lines = file_in.readlines()

file_out = open(output_filename, 'w')

result=[]
mapping_chars= {}
mapping_chars['a'] = '$'
mapping_chars['b'] = '$'
mapping_chars['c'] = '$'
mapping_chars['d'] = '$'
mapping_chars['e'] = '$'
mapping_chars['f'] = '$'
mapping_chars['g'] = '$'
mapping_chars['h'] = '$'
mapping_chars['i'] = '$'
mapping_chars['j'] = '$'
mapping_chars['k'] = '$'
mapping_chars['l'] = '$'
mapping_chars['m'] = '$'
mapping_chars['n'] = '$'
mapping_chars['o'] = '$'
mapping_chars['p'] = '$'
mapping_chars['q'] = 'z'
mapping_chars['r'] = '$'
mapping_chars['s'] = '$'
mapping_chars['t'] = '$'
mapping_chars['u'] = '$'
mapping_chars['v'] = '$'
mapping_chars['w'] = '$'
mapping_chars['x'] = '$'
mapping_chars['y'] = '$'
mapping_chars['z'] = 'q'
mapping_chars[' '] = ' '
mapping_chars['\n'] = ''

def update_mapping(google, normal):
	i = 0
	for cgoo in google:
		if cgoo in mapping_chars:
			mapping_chars[cgoo] = normal[i]
		i = i + 1
		
def getMap():
	return mapping_chars;
		
def change_to_normal(google):
	result = ''
	for cgoo in google:
		if cgoo in mapping_chars:
			result = result + mapping_chars[cgoo]
		else:
			result = result + '?'
	return result
	
update_mapping('ejp mysljylc kd kxveddknmc re jsicpdrysi','our language is impossible to understand')
update_mapping('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','there are twenty six factorial possibilities')
update_mapping('de kr kd eoya kw aej tysr re ujdr lkgc jv','so it is okay if you want to just give up')
	

i = 0
total_test_line = int(read_lines[i])
i=i+1
for j in range(0, total_test_line):
	normal_line = change_to_normal(read_lines[i])
	result.append('Case #'+str(j+1)+': '+normal_line+'\n')
	i=i+1
	
file_out.writelines(result)
file_out.close()
file_in.close()



print 'Updated mappings', mapping_chars

print "DONE!!"
