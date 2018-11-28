import string

sample_input = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z"
sample_output = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q"

translation_table = string.maketrans(sample_input, sample_output)

input_file = open("A-small.in")
output_file = open("A-small.out", "w")

input_file.readline()

count = 0

for line in input_file:
	count += 1
	translation = line.translate(translation_table)
	output_file.write("Case #" + str(count) + ": " + translation)

input_file.close()
output_file.close()