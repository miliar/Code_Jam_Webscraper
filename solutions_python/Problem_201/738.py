t = int(input())

for _ in range(t):
  n, k = map(int, input().split())
  a = {}
  s = set()
  cur_max_k = n
  a[cur_max_k] = 1
  s.add(cur_max_k)
  while (k > 0):
      cur_max = cur_max_k
      if (cur_max_k % 2 == 0):
        if (not (cur_max_k // 2) in s):
          a[cur_max_k // 2] = 0
          s.add(cur_max_k // 2)
        if (not (cur_max_k // 2 - 1) in s):
          a[cur_max_k // 2 - 1] = 0
          s.add(cur_max_k // 2 - 1)
        a[cur_max_k // 2] += a[cur_max_k]
        a[cur_max_k // 2 - 1] += a[cur_max_k]
      else:
        if (not (cur_max_k // 2) in s):
          a[cur_max_k // 2] = 0
          s.add(cur_max_k // 2)
        a[cur_max_k // 2] += 2 * a[cur_max_k]
      k -= a[cur_max_k]
      # print(a)
      del(a[cur_max_k])
      cur_max_k = max(a)
  print('Case #', _ + 1, ': ', cur_max // 2, ' ', cur_max // 2 - (cur_max % 2 == 0), sep = '')
    
