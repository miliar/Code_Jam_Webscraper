def is_recycle(x, position, max, l):
  m_str = str(max)
  x_str = ('%0' + str(l) + 'd') % x
  check_max = True
  check_min = True
  for i in range(0, l):
    x_digit = int(x_str[i])
    y_digit = int(x_str[(position+i)%l])
    m_digit = int(m_str[i])
    if check_max:
      if y_digit < m_digit:
        check_max = False
      if y_digit > m_digit:
        return (False, None)
    if check_min:
      if y_digit < x_digit:
        return (False, None)
      elif y_digit > x_digit:
        check_min = False
      elif i == l-1:
        return (False, None)
    if not check_max and not check_min:
      break
  return (True, (x, int(x_str[position:] + x_str[0:position])))

def count_recycle(a, b):
  recycle_set = set()
  l = len(str(b))
  max = b
  for x in range(a,b+1):
    for position in range(1,l):
      (yes, tuple) = is_recycle(x, position, max, l)
      if yes:
        recycle_set.add(tuple)
  return len(recycle_set)

#print count_recycle(1,2000000)

file_in = open('C-small-attempt0.in')
file_out = open('output.txt', 'w')
ncases = int(file_in.readline())
for case in range(1, ncases + 1):
  line = file_in.readline().split()
  a = int(line[0])
  b = int(line[1])
  result = 'Case #%d: %d\n' % (case, count_recycle(a,b))
  file_out.write(result)
file_out.close()
  