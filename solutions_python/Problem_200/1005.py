import numpy as np


def solve(n, j):
  front = 0
  for i in range(1, len(n)):
    if n[-i-1] > n[-i]:
      n[-i-1] -= 1
      front = i

  if front:
    n[-front:] = 9
  if not n[0]:
    n = n[1:]

  print('Case #{}: {}'.format(j+1, ''.join(map(str, n))))

def main():
  T = int(input())

  for i in range(T):
    solve(np.array(list(map(int, list(input())))), i)

if __name__ == '__main__':
    main()
