#http://code.google.com/codejam/contest/1460488/dashboard

input = open('A-small.in', 'r')
output = open('A-output.txt', 'w')
cases = int(input.readline())
origin = input.readlines()

goog = ['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q', ' ', '\n', '\'']
eng = ['a', 'x', 'o', 'n', 'k', 'e', 'p', 'm', 's', 'j', 'd', 'v', 'g',
'h', 'i', 't', 'q', 'w', 'b', 'f', 'u', 'r', 'c', 'l', 'y', 'z', ' ', '\n', '\'']

translated = []

for line in origin:
    new_line = list(line)
    for char in new_line:
        dex = goog.index(char)
        char = eng[dex]
        translated.append(char)
    
translated = "".join(translated)

eng = []

dex1 = 0
dex2 = 0
dex3 = 0

for char in translated:
    if char == '\n':
        dex2 = translated.index(char, dex3, len(translated))
        eng.append(str(translated[dex3:dex2]))
        dex3 = dex2 + 1
    dex1 += 1
    
eng.append(str(translated[dex3:]))

    
for x in xrange(cases):
    string = 'Case #%d: %s\n' % (x+1, eng[x])
    output.write(string)