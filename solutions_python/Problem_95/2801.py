input_1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi z q"
input_2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
input_3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

output_1 = "our language is impossible to understand q z"
output_2 = "there are twenty six factorial possibilities"
output_3 = "so it is okay if you want to just give up"

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def create_dict(input, output):
	retvals = {}
	counter = 0
	while counter < len(input):
		retvals[input[counter]]=output[counter]
		counter = counter + 1
	return retvals

def get_translator():
	translation = {}
	translation.update(create_dict(input_1, output_1))
	translation.update(create_dict(input_2, output_2))
	translation.update(create_dict(input_3, output_3))
	return translation

def find_missing(translation_codex):
	missing_values = []
	missing_keys = []
	for each in alphabet:
		if each not in translation_codex.values():
			missing_values.append(each)
		if each not in translation_codex.keys():
			missing_keys.append(each)
	return (missing_keys, missing_values)

def translate(input):
	codex = get_translator()
	counter = 0 
	output = ""
	while counter < len(input):
		output = "%s%s" % (output, codex[input[counter]])
		counter = counter + 1
	return output

def process_input_and_return_output(list_of_inputs): 
	counter = 1
	outputs = []
	for each in list_of_inputs:
		output_string = 'Case #%s: %s\n' % (counter, translate(each))
		print output_string
		outputs.append(output_string)
		counter = counter + 1
	return outputs

def get_inputs(file_name):
	f = open(file_name, 'r+')
	first = True
	return [line.partition('\n')[0] for line in f]
	f.close()


def translate_and_output(file_name):
	inputs = get_inputs(file_name)
	inputs.pop(0)
	print inputs
	f = open('codejamoutput.txt', 'w')
	for each in process_input_and_return_output(inputs):
		f.write(each)
	f.close()
	
	
	

		
