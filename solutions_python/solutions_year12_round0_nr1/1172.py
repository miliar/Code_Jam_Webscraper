import string
import sys
table = string.maketrans('ynficwlbkuomxsevzpdrjgthaq', 'abcdefghijklmnopqrstuvwxyz')

inp = open(sys.argv[1]);
outp = open(sys.argv[2], 'w');

count = int(inp.next())
i = 1;
for line in inp:
    outp.write("Case #%d: %s" % (i, string.translate(line, table)))
    i = i + 1
