def swap(c):
    if c == '+':
        return '-'
    else:
        return '+'

def flip(p, start, k):
    l = list(p)
    for i in range (start - 1, start + k - 1):
        l[i] = swap(l[i])
    return ''.join(l)

def flips(p, k):
    n = 0
    for i in range (0, len(p) - k + 1):
        if p[i] == '-':
            p = flip(p, i + 1, k)
            n = n + 1
    if '-' in p:
        return -1
    else:
        return n

t = int(input())
for i in range(1, t + 1):
  p, k = [s for s in input().split(" ")]
  n = flips(p, int(k))
  output = ""
  if n == -1:
      output = "IMPOSSIBLE"
  else:
      output = str(n)
  print("Case #{}: {}".format(i, output))
