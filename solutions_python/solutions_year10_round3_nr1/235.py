data = open('A.in', 'r').read().split('\n')

T = int(data.pop(0))

for t in range(T):
   wires = []
   inters = 0
   N = int(data.pop(0))
   for i in range(N):
      (a, b) = map(int, data.pop(0).split(' '))
      wires.append((a, b))
   wires.sort()

   for i in range(N):
      for j in range(i+1, N):
         if wires[j][1] < wires[i][1]:
            inters += 1

   print 'Case #' + str(t+1) + ': ' + str(inters)
