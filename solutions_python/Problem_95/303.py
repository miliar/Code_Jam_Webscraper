import sys

if_name, of_name = sys.argv[1:3]

map_samples="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz"

map_results="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq"

ifile = open (if_name,'r')
ofile = open (of_name,'w')

for i,l in enumerate(ifile):
    if i==0:
      continue
    ln = l.strip()
    s = ""
    for c in ln:
      s += map_results[map_samples.index(c)]
    ofile.write ('Case #%d: %s\n' % (i,s))

ifile.close()
ofile.close()
