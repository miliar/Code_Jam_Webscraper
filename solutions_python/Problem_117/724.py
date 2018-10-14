
import sys

def valid(lines):
   # Form reverse mapping of values to coordinates
   d = {}
   i = 0
   for line in lines:
      j = 0
      for c in line:
         if c not in d:
            d[c] = []
         d[c].append((i,j))
         j += 1
      i += 1
   # Search in ascending value order
   for n in sorted(d.keys()):
      for x, y in d[n]:
         if lines[x][y] == '.': # Cleared by equivalent value
            continue
         # Try to find row where all values are cleared or equal
         works = True
         for a in xrange(i):
            if lines[a][y] != '.' and lines[a][y] > n:
               works = False
               break
         if works:
            for a in xrange(i):
               lines[a][y] = '.'
         # Otherwise, try to find a column with same constraints
         else:
            works = True
            for a in xrange(j):
               if lines[x][a] != '.' and lines[x][a] > n:
                  works = False
                  break
            if works:
               for a in xrange(j):
                  lines[x][a] = '.'
            # No row or column can be mowed
            else:
               return False
   return True

def main():
   n = int(raw_input().strip())
   for t in xrange(n):
      (y, x) = raw_input().strip().split()
      (x, y) = (int(x), int(y))
      lines = []
      for l in xrange(y):
         toks = raw_input().strip().split()
         lines.append([int(i) for i in toks])
      if valid(lines):
         print 'Case #%d: YES' % (t+1,)
      else:
         print 'Case #%d: NO' % (t+1,)

if __name__ == '__main__':
   main()
