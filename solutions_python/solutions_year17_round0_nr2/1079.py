def minusone(l,pos):
  l[pos] = chr( ord(l[pos]) - 1)
  for i in range(pos,-1,-1):
    if (l[i] < '0'):
      l[i] = '9'
      l[i-1] = chr( ord(l[i-1]) - 1)
    else:
      break
  return l

def solution(last_num):
  tidy_num = list(last_num)
  pos = len(tidy_num) - 1
  while (pos > 0):
    if (tidy_num[pos] < tidy_num[pos - 1]):
      for i in range(pos,len(tidy_num)):
        tidy_num[i] = '9'
      tidy_num = minusone(tidy_num,pos - 1)    
    else:
      pos -= 1
  s = "".join(tidy_num)
  i = int(s)
  s = "%d" %i
  return s





t = int(raw_input())
for i in xrange(1, t + 1):
  pattern= raw_input()
  res = solution(pattern)
  case_str = "Case #%d: " %i
  print case_str + res
