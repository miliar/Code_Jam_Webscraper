import string
import sys
table = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'yhesocvxduiglbkrztnwjpfmaq')
for i in range(int(raw_input())):
    line = raw_input()
    print 'Case #%d: %s' % (i + 1, line.translate(table))

