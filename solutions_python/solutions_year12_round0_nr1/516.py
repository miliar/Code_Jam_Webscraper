from sys import argv
import string
try:
    f=open(argv[1])
except IOError:
    print "No such file: %s" % argv[1]
    exit()
except IndexError:
    print "No argument was given."
    exit()

abc='abcdefghijklmnopqrstuvwxyz'
yhe='yhesocvxduiglbkrztnwjpfmaq'
t=string.maketrans(abc,yhe)

T=int(f.readline())
for i in xrange(T):
    G=f.readline()
    S=G.translate(t)
    print "Case #%d: %s" % (i+1, S),

