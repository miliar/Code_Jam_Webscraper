import re
import codejam
import string

re_consonants = re.compile('[bcdfghjklmnpqrstvwxyz]')
def substr(string):
    j = 1
    while True:
        for i in range(len(string) - j+1):
            yield string[i:i+j]

        if j == len(string):
            break

        j += 1

for case in xrange(codejam.readint()):
    name, L = codejam.readstring().split()
    L = int(L)
    name = re_consonants.sub('X', name.lower())
    match = 'X' * L

    count = 0
    for substring in substr(name):
        if match in substring:
            count += 1
#    count = 0
#    match_idx = name.find(match)
#    length = len(name)
#    while match_idx >= 0:
#        match_idx * (length - match_idx - 
#        match_idx = name.find(match, match_idx + 1)
#        #count += 1 
#        #re.findall(match, name)
#        #for i in xrange(len(name)):
#        #    substring = name[i:]
#        #    substring2 = name[:-i]
#        #    print substring, substring2
#        #    if match in substring:
#        #        count += 1
#
    print "Case #%d: %d" % (case + 1, count)
