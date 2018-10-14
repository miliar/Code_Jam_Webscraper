import sys
import itertools

T = int(sys.stdin.readline())

for t in range(1, T+1):
   line = sys.stdin.readline().strip().split(' ')
   N = int(line[0])
   S = int(line[1])
   p = int(line[2])
   points = line[3:]

   regular_best = []
   surprising_best = []
   index = 0
   for point in points:
      for i in range(0, 11):
         for j in range(0, 11):
            for k in range(0, 11):
               if i + j + k == int(point) and abs(i-j) <= 2 and abs(i-k) <= 2 and abs(j-k) <= 2:
                  if (abs(i-j) == 2 or abs(i-k) == 2 or abs(j-k) == 2) and max(i, j, k) >= p:
                     if index not in surprising_best:
                        surprising_best.append(index)
                  elif max(i, j, k) >= p:
                     if index not in regular_best:
                        regular_best.append(index)
      index += 1

   best = -1
   surprising_size = min(len(surprising_best), S)
   regular_size = min(len(regular_best), N-S)

   for s in itertools.combinations(surprising_best, surprising_size):
      for r in itertools.combinations(regular_best, regular_size):
         if len(list(set(s) & set(r))) == 0:
            scores = len(s) + len(r)
            if scores > best:
               best = scores

   if best == -1:
      best = len(regular_best)

   print "Case #%d: %d" % (t, best)