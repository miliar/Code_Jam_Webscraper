f = open('D-large.in', 'r')
#f = open('D-small-attempt2.in', 'r')
#f = open('D-practice.in', 'r')
out = open('D.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
  N = int(f.readline().strip())
  array = [(int(x) - 1, (i + 1) == int(x)) for i, x in enumerate(f.readline().strip().split())]

  def count_cycle(start_index):
    count = 1
    current_index = array[start_index][0]
    array[current_index] = (array[current_index][0], True)
    while current_index != start_index:
      current_index = array[current_index][0]
      array[current_index] = (array[current_index][0], True)
      count += 1
    return count
  
  total = 0
  for i in xrange(N):
    if not array[i][1]:
      length = count_cycle(i)
      total += length 
  
  print 'Case #%d: %.6f' % (t + 1, total)
  out.write('Case #%d: %.6f' % (t + 1, total) + '\n')

f.close()
out.close()
