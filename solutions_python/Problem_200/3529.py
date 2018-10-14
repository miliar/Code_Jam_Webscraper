import sys
#def flip(i, k):
  # test
#  if '-' not in i:
#    return 0
#  l = i.split('')
#  p_c, m_c = 0, 0
#  for c in l:
#    if c == '+':
#      p_c += 1
#    else:
#      m_c += 1
#  if p_c % k != 0 and m_c % k != 0:
#    return 'IMPOSSIBLE'
#  far_left = 0
#  while True:
#    if s[far_left] == '-':
#      break
#    else:
#      far_left += 1
#  count = 0
#  end = False
#  while not end:
#    x = far_left
#    s = l[far_left:far_left+k]
#    print(s)
#    if len(s) < k:
#      return 'IMPOSSIBLE'
#    for c in s:
#      if c == '-':
        
def last_tidy(n):
  s = str(n)
  l = list(s)
  f_i = 0
  f_d = int(s[f_i])
  for i in range(f_i, len(s)-1):
    assert f_d != 0
    print(i, f_i, f_d, s[i+1])
    if int(s[i+1]) > f_d:
      f_i = i+1
      f_d = int(s[f_i])
      continue
    elif int(s[i+1]) == f_d:
      continue
    else:
      print('hi')
      f_d -= 1
      l[f_i] = str(f_d)
      l[f_i+1:] = ['9' for _ in range(len(s)-1-f_i)]
      break
  return int(''.join(l))


TEST = False
if len(sys.argv) == 2 and TEST:
  s = sys.argv[1]
  print(last_tidy(s))
elif len(sys.argv) == 2:
  f = open(sys.argv[1])
  out = open(sys.argv[1].replace('.in', '.out'), 'w')
  next(f)
  for i, l in enumerate(f):
    s = int(l)
    out.write('Case #{}: {}\n'.format(i+1, str(last_tidy(s))))
  out.close()
  f.close()

