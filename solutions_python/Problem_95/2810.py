'''
Created on Apr 14, 2012

@author: jyonkov
'''

a = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz"
b = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq"
d = dict(map(lambda x,y: (x,y),a,b))

n = int(raw_input())
for i in range(n):
    print "Case #{}: {}".format(i+1,''.join(map(lambda x:d[x],raw_input())))
