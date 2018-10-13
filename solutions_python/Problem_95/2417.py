import sys
from string import maketrans

intab = "yeqz"
outab = "aozq"
intab += "ejp mysljylc kd kxveddknmc re jsicpdrysi"
outab += "our language is impossible to understand"
intab += "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
outab += "there are twenty six factorial possibilities"
intab += "de kr kd eoya kw aej tysr re ujdr lkgc jv"
outab += "so it is okay if you want to just give up"

trantab = maketrans(intab, outab)
N = int(sys.stdin.readline())

for case in xrange(1, N+1):
    line = sys.stdin.readline()
    if line[-1] == "\n":
        line = line[:-1]
    sys.stdout.write("Case #"+str(case)+": "+line.translate(trantab))
    if case != N:
        sys.stdout.write("\n")
    
    
    
