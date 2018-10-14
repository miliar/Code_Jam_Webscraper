t = int(raw_input())
for caseNum in range(t):
   n = int(raw_input())
   lines = []
   for i in range(n):
      lines.append( tuple(map(int, raw_input().split())) )
   count = 0
   for i, a in enumerate(lines):
      starta, stopa = a
      for j, b in enumerate(lines[i:]):
         startb, stopb = b
         
         if (starta > startb and stopa < stopb) or (starta < startb and stopa > stopb):
            count += 1
   
   print "Case #%d: %d" % (caseNum+1, count)