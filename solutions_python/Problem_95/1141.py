import string

trans = 'yhesocvxduiglbkrztnwjpfmaq'
table = string.maketrans(string.ascii_lowercase, trans)

fin = open('in', 'r')
s = fin.read()
fin.close()

lines = s.split('\n')
lines = lines[1:]

fout = open('out', 'w')
for i, line in enumerate(lines):
    print line
    fout.write('Case #' + str(i+1) + ': ' + line.translate(table) + '\n')
    print 'Case #' + str(i+1) + ' ' + line.translate(table) + '\n',
fout.close()    
