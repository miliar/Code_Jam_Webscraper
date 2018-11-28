# Date:2012-04-14
# Author: Chika
import string

TRANS_TABLE = string.maketrans("ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvzq", "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upqz")

with open("A-small-attempt2.in") as infile:
    T = int(infile.readline())

    with open("A-small-attempt2.out", "w") as outfile:
        for i in range(T):
            G = infile.readline()
            outfile.write("Case #%d: %s" % (i+1, string.translate(G, TRANS_TABLE), ))
