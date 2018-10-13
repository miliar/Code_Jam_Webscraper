import sys

def minimize(C, F, X):
  min = X/2.0
  n = 1
  while True:
    t = 0.0
    r = 2.0
    for i in range(n):
      if i < n-1:
        t += C/r
        r += F
      else:
        t += X/r
    if t > min:
      return min
    min = t
    n += 1

if __name__ == '__main__':
  T = int(sys.stdin.readline())
  for i in range(1,T+1):
    C, F, X = map(float, sys.stdin.readline().split())
    print('Case #{0}: {1:.6f}'.format(i, minimize(C, F, X)))

