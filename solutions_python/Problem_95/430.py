#!/usr/bin/python
from __future__ import print_function

from string import maketrans
import sys;

intab = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz"
outta = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq"
#trantab = maketrans(outta, intab)
trantab = maketrans(intab, outta)

T = int(sys.stdin.readline());

for t in xrange(0,T):
    lin = sys.stdin.readline().rstrip('\n');
    print ("Case #",(t+1),": ",lin.translate(trantab), sep='');
