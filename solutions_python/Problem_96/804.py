import itertools

f = open('B-small-attempt0.in')

line = f.readline()
num_lines = int(line[:-1])

for line_num in xrange(num_lines):
  line = f.readline()[:-1]
  p_line = line.split(' ')
  N = int(p_line[0])
  S = int(p_line[1])
  p = int(p_line[2])
  cnt = 0
  for i in xrange(3,N+3):
    result = int(p_line[i])
    if result == 0:
      if p == 0:
        cnt += 1
    else:
      possibilities = []
      for x in xrange(5):
        if (result+x) % 3 == 0 and (result+x)/3 < 11 and (result+x)/3 > -1:
          if possibilities != [] and max(possibilities) < p and ((x == 3) or (x == 4)):
            if S > 0:
              possibilities.append((result+x)/3)
              S -= 1
          else:
            possibilities.append((result+x)/3)
      if max(possibilities) >= p:
        cnt += 1
    
  print 'Case #%d: %d' % (line_num+1, cnt)

    
    