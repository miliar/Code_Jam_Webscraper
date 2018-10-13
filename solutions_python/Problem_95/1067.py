import string


dic = "yhesocvxduiglbkrztnwjpfmaq"


source = open('input.in')
source_str = source.read()
source_list = source_str.split('\n')
source.close()

input_num = int(source_list[0])
source_list = source_list[1 : len(source_list) - 1]

f = open('A-small.out', 'w')
line = 1
for node in source_list:
    out = []
    for char in node:
        if char != ' ':
            out.append(dic[ord(char) - ord('a')])
        else:
            out.append(char)

    out = string.join(out, '')
    f.write("Case #" + str(line) + ": " + str(out) + '\n')
    line = line + 1
f.close()      
