import string

googlerese = 'ynficwlbkuomxsevzpdrjgthaq'
english =    'abcdefghijklmnopqrstuvwxyz'
trans = string.maketrans(googlerese, english)

input_file = open('input.in', 'r')
output_file = open('output.txt', 'w')

lines = input_file.readlines()
input_file.close()

cases = int(lines[0])
cases = 30 if cases > 30 else cases

for case in range(cases):
    line = lines[case + 1]
    translated_line = "Case #" + str(case+1) + ": " + line.translate(trans)
    output_file.write(translated_line)
