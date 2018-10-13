import StringIO, string, sys

if len(sys.argv)>1:
    input = file(sys.argv[1])
else:
    input = StringIO.StringIO("""3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv""")

trans = string.maketrans("ynficwlbkuomxsevzpdrjgthaq",
                         "abcdefghijklmnopqrstuvwxyz")
for i in range(int(input.readline())):
    print "Case #%d: %s" % (i+1,
                            input.readline().strip().translate(trans))

