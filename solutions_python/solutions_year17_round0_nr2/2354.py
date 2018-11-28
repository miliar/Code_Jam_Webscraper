
def solve(n):
  n = [int(x) for x in n]
  for x in range(0, len(n)-1, 1):
    if n[x] > n[x+1]:
       x = n.index(n[x])
       if n[x] == 0:
          n[x] = 9
          y = x-1
          while y >= 0:
            if n[y] == 0:
              n[y] = 9
              y -= 1
            else:
              n[y] -= 1
              break
       else:
         n[x] -= 1
       y = x+1
       while y < len(n):
         n[y] = 9
         y += 1
       break
  return ''.join([str(x) for x in n]).lstrip('0')

    

T = int(input())
for t in range(1, T+1):
  n = input()
  print('Case #{}: {}'.format(t, solve(n)))

