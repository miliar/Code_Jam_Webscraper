a = open('input').read().split('\n')[:-1]
f = open('output', 'w')
for i in range(1, int(a[0]) + 1):
      print('Case #' + str(i) + ': ', sep = '', end = '', file = f)
      ans = 0
      x, y = map(int, a[i].split())
      for n in range(x, y + 1):
            st = str(n)
            temp = set()
            for shift in range(1, len(st)):
                  m = int(st[-shift:] + st[:-shift])
                  if n < m <= y:
                        temp.add(m)
            ans += len(temp)
      print(ans, sep = '', end = '\n', file = f)
