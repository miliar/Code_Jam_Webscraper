import sys
import re
code = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz\n'
s ='ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq\n'
dict = {}

for i, ch in enumerate(s):
    dict[ch] = code[i]

if len(sys.argv) < 3:
    raise Exception('error arg',  'file name not found')
fr=None
fw=None
try:
    fr = open(sys.argv[1], 'r')
    fw = open(sys.argv[2], 'w')
    T = int(re.split('\D+',  fr.readline())[0])
    i = 1
    while (T>=i):
        line = fr.readline()
        newline ='Case #{0}: {1}'.format(i, ''.join([dict[ch] for ch in line]))
        fw.write(newline)
        i=i+1
finally:
    if fr!=None:
        fr.close()
    if fw!=None:
        fw.close()
