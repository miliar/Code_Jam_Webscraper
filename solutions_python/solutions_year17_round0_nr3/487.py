def score(x):
  if x == 0:
    return (0, 0)
  else:
    return (x-x//2, x//2)

def solve(N, K):
  #print('Solving', N, K)
  c = [0, 0]
  v = [0, 0]
  L = N-1
  c[L%2] = 1
  v[L%2] = L
  count = 0
  level = 0
  while count + 2 ** level < K:
    count += c[0] + c[1]
    level += 1
    old_v = v
    old_c = c
    v = [0, 0]
    c = [0, 0]
    for i in (0, 1):
      if old_c[i] != 0:
        if old_v[i] == 1:
          v[0] = 0
          c[0] += old_c[i]
        else:
          if old_v[i] % 2 == 0:
            val = (old_v[i] // 2) - 1
            v[val % 2] = val
            c[val % 2] += 2 * old_c[i]
          else:
            val = (old_v[i] // 2)
            assert c[val % 2] == 0 or v[val % 2] == val
            v[val % 2] = val
            c[val % 2] += old_c[i]
            val -= 1
            v[val % 2] = val
            c[val % 2] += old_c[i]
    #print(c, v)
  #print('N, K = ', N, K, '. Level', level, 'Counts {}: {}, {}: {}.'.format(v[0], c[0], v[1], c[1]), 'Node count:', count, 'Next level:', count + 2**level)
  assert c[0] == 0 or c[1] == 0 or v[0] != v[1]
  if v[0] < v[1]:
    c = c[::-1]
    v = v[::-1]

  c[0] -= (K - count)
  if c[0] >= 0:
    return score(v[0])
  else:
    assert c[1] + c[0] >= 0
    return score(v[1])
  

T = int(input())

for TT in range(T):
  N, K = map(int, input().split())
  M, m  = solve(N, K)
  print("Case #{}: {} {}".format(TT + 1, M, m))
