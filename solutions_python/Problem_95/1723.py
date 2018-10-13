import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()[1:]

english = 'abcdefghijklmnopqrstuvwxyz '
google =  'ynficwlbkuomxsevzpdrjgthaq '

new_lines = ['']
index = 0
for line in lines:
    for c in line:
        if c != '\n':
            i = google.index(c)
            new_lines[index] += english[i]
    index += 1
    new_lines.append('')

for i in range(len(new_lines) - 1):
    print 'Case #' + str(i+1) + ': ' + new_lines[i]
