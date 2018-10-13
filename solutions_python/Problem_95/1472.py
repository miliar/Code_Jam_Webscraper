import sys
import string

# q x

intab  = 'abcdefghijklmnopqrstuvwxyz '
outtab = 'yhesocvxduiglbkrztnwjpfmaq '
trantab = string.maketrans(intab, outtab)

_ = sys.stdin.readline()
for i, line in enumerate(sys.stdin.readlines()):
    print 'Case #%d: %s' % (i+1, line.rstrip().translate(trantab))
