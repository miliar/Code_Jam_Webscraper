f = open('1.in')
out = open('1.out', 'w')

count = int(f.readline())

for num in range(count):
  numOnThisLine = int(f.readline())
  nums = f.readline().split(' ')
  
  xor = 0
  tot = 0
  least = 1000000000
  for readNum in nums:
    xor = xor ^ int(readNum)
    tot += int(readNum)
    least = min(least, int(readNum))

  if xor == 0:
    out.write('Case #' + str(1+num) + ": " + str(tot - least) + '\n')
  else:
    out.write('Case #' + str(1+num) + ": " + "NO\n")

f.close()
out.close()
