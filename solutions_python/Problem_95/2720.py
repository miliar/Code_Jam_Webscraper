alph = 'abcdefghijklmnopqrstuvwxyz '
beph = 'yhesocvxduiglbkrztnwjpfmaq '
strings = []
cases = raw_input()
for x in range(int(cases)):
    strings.append(raw_input())
count = 1
for x in strings:
    temp = ''
    for y in range(len(strings[strings.index(x)])):
        temp += beph[alph.index(strings[strings.index(x)][y])]
    print 'Case #'+str(count)+': ' + temp
    count = count + 1
