def flip(cakes, start, end):
  while start <= end:
    if cakes[start] == '-':
      cakes[start] = '+'
    else:
      cakes[start] = '-'
    start=start+1


f = open('A-large.in', 'r')
t = int (f.readline())

for c in xrange(1, t + 1):
  count = 0
  line = f.readline().strip()
  items = line.split(" ")
  cakes = list(items[0])
  size = int(items[1])
  prev = ''
  if (len(cakes) >= size):
    i = 0
    j = len(cakes)-size
    end = len(cakes) - 1
    size_1 = size - 1
    while (i <= j):
      while (i <= j and cakes[i] != '-'):
        i=i+1
      if (i<j):
        flip(cakes, i, i+size_1)
        count+=1
      while (end >= size_1 and cakes[end] != '-'):
        end=end-1
      if(end >=size_1):
        flip(cakes, end-size_1, end)
        count+=1
      i=i+1
      end=end-1

  flag = None
  for currcake in cakes:
    if currcake == '-':
      flag = True
  if flag == True:
    print "Case #{}: IMPOSSIBLE".format(c)
  else:
    print "Case #{}: {}".format(c, count)
