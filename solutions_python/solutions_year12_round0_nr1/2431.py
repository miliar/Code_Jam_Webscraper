n = 3
dic = {}
dic['q'] = 'z'
dic['z'] = 'q'
while n != 0:
  n -= 1
  a = raw_input()
  b = raw_input()
  i = 0
  while i < len(a):
    if a[i] == ' ':
      i += 1
      continue
    dic[a[i]] = b[i]
    i += 1

n = int(raw_input())
i = 1
while i <= n:
  s = raw_input()
  out=''
  for ch in s:
    if ch == ' ':
      out += ' '
    else:
      out += dic[ch]
  print "Case #%d: %s" %(i, out)
  i += 1
