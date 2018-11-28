
def solve(translation_dictionary, sentence):
    solution = ''
    for c in sentence:
        if c in translation_dictionary:
            solution += translation_dictionary[c]
        else:
            print c, "is missing from translation"
            print solution, sentence
    return solution


code = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
translation = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"
translation_dictionary = {'y':'a','e':'o','q':'z','z':'q'}

for x in range(len(code)):
    if code[x] not in translation_dictionary:
        translation_dictionary[code[x]] = translation[x]

k = translation_dictionary.keys()
k.sort()
s = translation_dictionary.values()
s.sort()
print k
print s
print translation_dictionary


fin = file('A-small-attempt5.in', 'r')
fout = file('file.out', 'w')
count = int(fin.readline())
for c in range(count):
    sentence = fin.readline().strip('\n')
    solution = solve(translation_dictionary, sentence)
    fout.write('Case #%d: %s\n' % (c+1, solution))