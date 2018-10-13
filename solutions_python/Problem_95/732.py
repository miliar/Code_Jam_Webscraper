from string import maketrans
from string import translate

my_trans = maketrans('''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvzq''',
'''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upqz''')

outputlist = []

for i, G in enumerate(open('A-small-attempt0.in', 'r').read().splitlines()[1:]):
    outputlist.append('Case #%i: %s' % \
                      (i+1, translate(G, my_trans)))
    
outputfile = open('SpeakingInTonguesOutput.txt', 'w')

outputfile.write( '\n'.join(outputlist) )