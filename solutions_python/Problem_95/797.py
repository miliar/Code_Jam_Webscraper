import sys, string

def decodetable():
    src="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz"
    trg="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq"
#    checksrc = {}
#    for c in src:
#        checksrc[c] = 1
#    checktrg = {}
#    for c in trg:
#        checktrg[c] = 1
#    for n in range(ord('a'), ord('z')+1):
#        if not checksrc.get(chr(n)):
#            print "letter", chr(n), "is missing in source"
#        if not checktrg.get(chr(n)):
#            print "letter", chr(n), "is missing in target"
#
#    print len(checksrc), "letters in source"
#    print string.maketrans(src, trg)
    return string.maketrans(src, trg)

def main(args):
    table = decodetable()
    f = file(args[1])
    ncases = int(f.readline())
    for i in range(ncases):
        line = f.readline()
        line = line.rstrip()
        line = line.translate(table, "\r\n")
        sys.stdout.write("Case #%d: %s\n" % (i+1, line))

if __name__ == "__main__":
    main(sys.argv)