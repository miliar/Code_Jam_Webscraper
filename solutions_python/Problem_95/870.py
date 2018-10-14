sin = 'ejp mysljylc kd kxveddknmc re jsicpdrysi\n'
sin += 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
sin += 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

sout = 'our language is impossible to understand\n'
sout += 'there are twenty six factorial possibilities'
sout += 'so it is okay if you want to just give up'

dic = {}

for i in xrange(len(sin)):
  dic[sin[i]] = sout[i]

dic['z'] = 'q'
dic['q'] = 'z'



f = open('A-small-attempt0.in')

line = f.readline()
num_lines = int(line[:-1])

for line_num in xrange(num_lines):
  line = f.readline()[:-1]
  out_line = ''
  for c in line:
    out_line += dic[c]
  print 'Case #%d: %s' % (line_num+1, out_line)
