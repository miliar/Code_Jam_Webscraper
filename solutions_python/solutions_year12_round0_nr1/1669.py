from sys import stdin as input
import string
 
trans = string.maketrans('ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv q z','our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up z q')

for i in range(int(input.readline())):
    
    print "Case #%d: %s" % ((i+1),input.readline().strip().translate(trans))