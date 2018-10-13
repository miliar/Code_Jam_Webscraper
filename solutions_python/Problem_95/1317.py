''''Google CodeJam 2012 Qualification Round Part A'''
import sys
from string import maketrans

# The examples provided covered the whole alphabet except q/z, which must map to each other
example_in = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv qz'''
example_out = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up zq'''

# Include uppercase
example_in  += example_in.upper()
example_out += example_out.upper()

translator = maketrans(example_in, example_out)

sys.stdin.next()
for number, line in enumerate(sys.stdin):
	line = line.strip('\n')
	print 'Case #%d: %s' % (number+1, line.translate(translator))
