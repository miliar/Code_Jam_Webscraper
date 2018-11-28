import string

crypt = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

clear = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

dictionary = dict()
dictionary['a']='y'
dictionary['o']='e'
dictionary['z']='q'
dictionary['q']='z'

for i in xrange(len(crypt)):
    if crypt[i] in string.lowercase:
        dictionary[crypt[i]] = clear[i]

f = open("input",'r')
file = f.readlines()

ctr = 0
for line in file:
    if ctr == 0:
        ctr += 1
        continue
    newline = "Case #" + str(ctr) + ": "
    for char in line:
        if char in string.lowercase:
            newline+= dictionary[char]
        else:
            newline+= char
    print newline,
    ctr += 1
