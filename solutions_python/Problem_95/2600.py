dictionary = {}

stringa = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
aslia = 'our language is impossible to understand'
stringb = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
aslib = 'there are twenty six factorial possibilities'
stringc = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
aslic = 'so it is okay if you want to just give up'

for ii in xrange(len(stringa)):
    dictionary[stringa[ii]] = aslia[ii]
for ii in xrange(len(stringb)):
    dictionary[stringb[ii]] = aslib[ii]
for ii in xrange(len(stringc)):
    dictionary[stringc[ii]] = aslic[ii]

key = dictionary.keys()
dictionary['z'] = 'q'
dictionary['q'] = 'z'
dictionary[' '] = ' '
dictionary['\n'] = ''

##for kk in sorted(key):
##    print kk, dictionary[kk]

namafile = 'A-small-attempt1.in'
ff = open(namafile, 'r')

num_case = int(ff.readline())

ff_out = open('a.out', 'w')

for ii in xrange(num_case):
    line = ff.readline()
    sol = ''
    for char in line:
        sol = sol + dictionary[char]
    ff_out.write('Case #'+str(ii+1)+': '+sol+'\n')

ff.close()
ff_out.close()