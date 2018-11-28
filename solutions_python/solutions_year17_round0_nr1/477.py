
def happy(c):
  return c == '+'

def op(c):
  if c == '+':
    return '-'
  else:
    return '+'

def flip(s, x, K):
  assert x >= 0 and x < len(s)
  for i in range(x, x + K):
    s[i] = op(s[i])
  return s



def solve(s, K, N):
  if K > N:
    return all(map(happy, s))

  count = 0
  for i in range(0, N-K+1):
    j = N-i-1
    assert j >= K-1
    if not happy(s[i]):
      s = flip(s, i, K)
      count += 1
    if not happy(s[j]):
      s = flip(s, j-K+1,  K)
      count += 1
  return count, all(map(happy, s))



T = int(input())

for TT in range(T):
  inp = input().split()
  count, h = solve(list(inp[0]), int(inp[1]), len(inp[0]))
  if not h:
    res = "IMPOSSIBLE"
  else:
    res = count
    
  print("Case #{}: {}".format(TT + 1, res))
