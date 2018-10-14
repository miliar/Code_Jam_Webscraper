import sys
from string import maketrans

english, googlish = 'abcdefghijklmnopqrstuvwxyz', 'yhesocvxduiglbkrztnwjpfmaq'
trans = maketrans(english, googlish)

fin, fout = sys.stdin, sys.stdout
try:
    n = int(fin.readline())
    for i in xrange(n):
        ln = fin.readline()
        lnout = "Case #%d: %s" % (i +1, ln.translate(trans))
        fout.writelines([lnout])
finally:
    fout.close()
    fin.close()