#!/usr/bin/python -tt
def main():
  t1 = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''
  t2 = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''
  d = {}
  for i in xrange(len(t1)):
    d[t1[i]] = t2[i]
  d['z'] = 'q'
  d['q'] = 'z'
  inf = open('input.txt', 'r')
  outf = open('output.txt', 'w')
  n = int(inf.readline())
  for i in xrange(n):
    outf.write('Case #%d: ' % (i+1))
    l = inf.readline()
    for c in l:
      if c in d: outf.write(d[c])
      else: outf.write(c)
  
if __name__ == '__main__':
  main()
