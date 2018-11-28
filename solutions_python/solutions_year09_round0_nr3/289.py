import sys

phrase = 'welcome to code jam'
plen = len(phrase)

def find_next(line, i):
  here = 0
  if i == plen - 1:
    return line.count(phrase[-1])
  for pos, c in enumerate(line):
    if c == phrase[i]:
      here += find_next(line[pos + 1:], i + 1)
  return here

input_file = sys.argv[1]
f = open(input_file, 'r')
N = int(f.readline())
print N

fw = open('codejam_q3.out', 'w')

for i in range(N):
  line = f.readline().strip()
  cnt = find_next(line, 0)
  print 'Case #%d: %04d' % (i + 1, cnt % 10000)
  fw.write('Case #%d: %04d\n' % (i + 1, cnt % 10000))

fw.close()
f.close()
