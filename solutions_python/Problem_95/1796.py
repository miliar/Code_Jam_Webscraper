translation_dict = {'a':'y', 'o':'e', 'z':'q', 'q':'z'}

examples = {'ejp mysljylc kd kxveddknmc re jsicpdrysi':'our language is impossible to understand', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd':'there are twenty six factorial possibilities','de kr kd eoya kw aej tysr re ujdr lkgc jv':'so it is okay if you want to just give up'}

for key,val in examples.items():
		for char_idx in range(len(key)):
			translation_dict[key[char_idx]] = val[char_idx]

def translate_to_english(text):
	output_arr = [];
	for char_idx in range(len(text)-1):
		output_arr.append(translation_dict[text[char_idx]])
	return ''.join(output_arr)

reader = open('small1.in', 'r')
writer = open('small1.out', 'w')
num_lines = int(reader.readline())
for input_number in range(1, num_lines+1):
	line = reader.readline()
	writer.write('Case #'+str(input_number)+": "+translate_to_english(line)+'\n')