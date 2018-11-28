import numpy as np


def solve(S, K, j):
  switch = 0
  l = len(S)

  for i in range(l - K + 1):
    if not S[i]:
      switch += 1
      S[i:i+K] = np.logical_not(S[i:i+K])

  print('Case #{}: {}'.format(j,
                              switch if all(S[l-K+1:]) else 'IMPOSSIBLE'))


def main():
    T = int(input())

    for i in range(T):
      S, K = input().split(' ')
      S = np.array([True if c == '+' else False for c in S], dtype=bool)
      K = int(K)
      solve(S, K, i+1)


if __name__ == '__main__':
    main()
