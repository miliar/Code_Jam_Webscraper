def howMany(n, stng):
   sum = 0
   added = 0
   for i in range(n+1):
      if sum < i:
         added += i - sum
         sum = i
      sum += int(stng[i])
   return added
file = open('inputA.txt', 'r')
out = open('outputA.txt', 'w')
num = int(file.readline().strip())
for i in range(num):
   nxt = file.readline().strip().split(' ')
   n = int(nxt[0])
   stng = nxt[1]
   out.write('Case #'+str(i+1)+': ' + str(howMany(n, stng)) + '\n')
file.close()