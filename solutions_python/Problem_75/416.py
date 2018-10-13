import sys

def my_opposed(r2, result, elem) :
   i = 0
   l = len(result)
   while i < l :
      s1 = elem + result[i]
      s2 = result[i] + elem
      if (s1 in r2) or (s2 in r2) :
         return True
      i += 1
   return False

def my_invoke(r1, r2, v) :
   i = 0
   l = len(v)
   r1f = [x[0:2] for x in r1]
   r1t = [x[2] for x in r1]
   result = ''
   while i < l :
      if len(result) == 0 :
         result += v[i]
	 i += 1
	 continue
      s1 = v[i] + result[-1]
      s2 = result[-1] + v[i]
      if s1 in r1f :
         result = result[:-1] + r1t[r1f.index(s1)]
      elif s2 in r1f :
         result = result[:-1] + r1t[r1f.index(s2)]
      elif my_opposed(r2, result, v[i]) :
         result = ''
      else :
         result += v[i]
      i += 1
   fmt = '['
   for x in result[:-1] :
      fmt = fmt + x + ', '
   if len(result) > 0 :
      fmt = fmt + result[-1]
   fmt = fmt + ']'
   return fmt

if __name__ == '__main__' :
   t = int(sys.stdin.readline())
   i = 1
   while i <= t :
      line = sys.stdin.readline().split()
      c = int(line[0])
      d = int(line[c+1])
      n = int(line[c+d+2])
      r1 = line[1:1+c]
      r2 = line[2+c:2+c+d]
      v = line[3+c+d]
      print 'Case #%d:' % i, my_invoke(r1, r2, v)
      i += 1
