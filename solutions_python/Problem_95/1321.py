#!/bin/python
i = open('A-small-attempt3.in')
o = open('code.out','w')

a="""ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"""

b="""our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"""


rosetta = {
    "a": "y",
    #"o": "e",
    "y": "a",
    "z": "q",
    "q": "z",
}

for index,x in enumerate(a.replace(' ','')):
    if not x in rosetta:
        rosetta[x]=b.replace(' ','')[index]

for t in range(int(i.readline())):
    g = i.readline().strip()
    gout = ''
    for x in g:
        if x ==' ':
            gout+=" "
        else:
            gout+=rosetta[x]
    o.write("Case #%d: "%(t+1) +gout+"\n")

i.close()
o.close()