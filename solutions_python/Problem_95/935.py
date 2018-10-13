'''
'''

###########################################################
# function defs
###########################################################

cur_dict = {'a':'y','o':'e','z':'q'}
crypt = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
trans = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
for ci in range(len(crypt)):
	cur_dict[crypt[ci]] = trans[ci]
for c in range(97,97+26):
	if not chr(c) in cur_dict.keys():
		miss_k = chr(c)
	if not chr(c) in cur_dict.values():
		miss_v = chr(c)
cur_dict[miss_k] = miss_v

print cur_dict

###########################################################
# input
###########################################################

input_file = 'A-small-attempt0.in.txt'
#input_file = '-large.in.txt'
input_data = open(input_file,'r').readlines()

###########################################################
# cases
###########################################################

output = ''
num_cases = int(input_data[0])
i = 1
for n in range(num_cases):
	line = input_data[i].rstrip()
	i += 1
	s=''
	for c in line:
		s+=cur_dict[c]
	output += 'Case #%d: %s\n'%(n+1,s)

###########################################################
# output
###########################################################

outfile = open('output_small.txt','w')
#outfile = open('output_large.txt','w')
outfile.write(output)
outfile.close()