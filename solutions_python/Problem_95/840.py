import sys

fname = sys.argv[1]

#import re
#re.split('[eioau]', 'qwertyjukilop')

def itero(fn):
    with open(fname) as f:
        i = 0
        for line in f:
            if i > 0:
                x = line.strip()
                fn(i, x)
            i += 1

xA = 'our language is impossible to understand' 'there are twenty six factorial possibilities' 'so it is okay if you want to just give up'
xB = 'ejp mysljylc kd kxveddknmc re jsicpdrysi' 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd' 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
XX = dict(set(map(None, xB, xA)))      
XX.update( { 'q' : 'z', 'z' : 'q' })

def problemA(i, s):
    #r = "".join(map(lambda i: XX[i], list(s)))
    r = "".join(map(lambda i: XX[i], list(s)))
    print ("Case #%i:" % i), r


                  
itero(problemA)



