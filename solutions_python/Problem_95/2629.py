from string import maketrans

english =    'abcdefghijklmnopqrstuvwxyz'
googlerese = 'ynficwlbkuomxsevzpdrjgthaq'

translation = maketrans(googlerese,english)

f = open('/Users/mwrigley83/documents/A-small-attempt7.in.txt')
output = open('/Users/mwrigley83/documents/output.txt','w')
x = 1
for line in f.readlines()[1:]:
    string = 'Case #%s: %s' % (x,line.translate(translation))
    output.write(string)
    x += 1

output.close()
