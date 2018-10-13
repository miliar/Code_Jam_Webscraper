f = open('/home/izuzak/Downloads/C-small-attempt1.in', 'r')
o = open('/home/izuzak/Downloads/out', 'w')
lines = f.readlines()[1:]

lineno = 1
for line in lines:
  l = line[:-1].split(' ')
  s = 'Case #' + str(lineno) + ': '
  
  A = int(l[0])
  B = int(l[1])
  count = 0
  for n in range(A, B):
    for m in range(n+1, B+1):
      for k in range(1, len(str(n))):
        string = str(m)
        new = int(string[-1*k:] + string[:-1*k])
        if (new == n):
          count = count + 1
          #print(n,m)
  
  o.write(s + str(count) + '\n')
  lineno = lineno + 1;
