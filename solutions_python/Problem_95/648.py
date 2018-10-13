import sys
from string import maketrans

N = int(sys.stdin.readline()[:-1])

s = 'yhesocvxduiglbkrztnwjpfmaq' 
d = 'abcdefghijklmnopqrstuvwxyz'
trantab = maketrans(d, s)

for i in range(N):
    line = sys.stdin.readline()[:-1]
    print "Case #%d: %s" % (i+1, line.translate(trantab))

