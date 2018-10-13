def half(n):
  return (n/2, n/2 + n%2 - 1)

def solve(n, k):
  if k == 1:
    return half(n)
  count = 1
  prev = [half(n)]
  new = []
  while count < k:
    new = []
    for L, R in prev:
      new.append(half(L))
      new.append(half(R))
    count += 2*len(prev)
    prev = new
  return sorted(new)[count - k]

if __name__ == '__main__':
  num_cases = int(raw_input())
  for case in range(num_cases):
    line = raw_input().split(' ')
    n = int(line[0])
    k = int(line[1])
    y, z = solve(n, k)
    print 'Case #{}: {} {}'.format(case+1, y, z)
