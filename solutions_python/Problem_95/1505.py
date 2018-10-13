#speaking in Tongues
import itertools 
f = open("A.in","r")
f2 = open("A.out","w")
f.readline()

O = "abcdefghijklmnopqrstuvwxyz "
R = "yhesocvxduiglbkrztnwjpfmaq "

i=1
for l in f:
    sentence = list(l.strip())
    for j in xrange(len(sentence)):
        sentence[j] = R[O.index(sentence[j])]
    f2.write( "Case #%d: %s\n" % (i,''.join(sentence)) )
    i+=1

f2.close()

f.close()
