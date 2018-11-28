alpha_dict = dict()


alpha_dict['a'] = 'y'
alpha_dict['o'] = 'e'
alpha_dict['z'] = 'q'
alpha_dict['q'] = 'z'

learn_text1 = [   
	'ejp mysljylc kd kxveddknmc re jsicpdrysi', 		\
	'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 	\
	'de kr kd eoya kw aej tysr re ujdr lkgc jv' 		\
	]	
learn_text2 = [
	'our language is impossible to understand',			\
	'there are twenty six factorial possibilities',		\
	'so it is okay if you want to just give up'			\
	]


for i in range(0,3):
	line = learn_text1[i]
	for j in range(0,len(line)):
		if line[j].isalpha():
			alpha_dict[line[j]] = learn_text2[i][j]

inputs_text = []

lines = int(raw_input())
for i in range(0,lines):
	line = raw_input()
	newline = []
	for j in range(0,len(line)):
		if line[j].isalpha():
			newline.append(alpha_dict[line[j]])
		else:
			newline.append(line[j])

	print 'Case #' + str(i+1) + ': ' + ''.join(newline)
