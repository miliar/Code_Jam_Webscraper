import re, sys

input_file = sys.argv[1]
f = open(input_file, 'r')

line = f.readline()
L, D, N = (int(x) for x in line.split())
print L, D, N

words = [f.readline().strip() for i in range(D)]
patterns = [f.readline().strip() for i in range(N)]

f.close()

fw = open('codejam_q1.out', 'w')
i = 0
for pattern in patterns:
  pattern = pattern.replace('(', '[').replace(')', ']')
  i += 1
  p = re.compile(pattern)
  matches = 0
  for word in words:
    if p.match(word):
      matches += 1
  print 'Case #%d: %d' % (i, matches)
  fw.write('Case #%d: %d\n' % (i, matches))

fw.close()
