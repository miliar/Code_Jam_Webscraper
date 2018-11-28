import numpy as np

def xand(a, b):
  return (a and b) or not (a or b)

def solve(n, k):
  if k == 1:
    return(int((n)//2), int((n-1)//2))
  return(solve(n//2, k//2) if n % 2 or not k % 2 else solve(n/2 - 1, k//2))


def main():
  T = int(input())

  for i in range(T):
    N, K = map(int, input().split())
    print('Case #{}: {} {}'.format(i+1, *solve(N, K)))

if __name__ == '__main__':
  main()
