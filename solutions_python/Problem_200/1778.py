f = open('B-large.in', 'r')
ff=open('B-large.out', 'w')
t = int(f.readline())
for i in range(t):
  n = list(f.readline().strip())
  last = 0
  for j in range(len(n)):
    if int(n[j]) < last:
      for k in range(len(n)):
        if int(n[k]) == last:
          n[k] = str(last - 1)
          break
      for l in range(k+1, len(n), 1):
        n[l] = '9'
    else:
      last = int(n[j])
  for j in range(len(n)):
    if not n[j] == '0':
      n = n[j:]
      break
  print(n)
  ff.write('Case #' + str(i+1) + ': ')
  for x in n:
    ff.write(x)
  ff.write('\n')
