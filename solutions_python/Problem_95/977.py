def translate(string):
    code_dict = {}
    translation = []
    strings_coded = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
    strings_decoded = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]
    for i in range(len(strings_coded)):
        for j in range(len(strings_coded[i])):
            code_dict[strings_coded[i][j]] = strings_decoded[i][j]
    code_dict['z'] = 'q'
    code_dict['q'] = 'z'
    for letter in string:
#        print("trying letter: %s" % letter)
        translation.append(code_dict[letter])
    return "".join(translation)

filePrefix = 'A-small-attempt0'
fin = open(filePrefix + '.in', 'r')
fout = open(filePrefix + '.out', 'w')
T = int(fin.readline())
#print(code_dict)
for i in range(T):
    line = fin.readline().strip()
    fout.write("Case #%d: %s\n" % ((i+1), translate(line)))
#print(sorted(list(code_dict.values())))