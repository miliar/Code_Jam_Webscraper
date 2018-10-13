#!/usr/bin/python

import queue

def solution(S, K):
  sequence = [c == '+' for c in S]
  result = 0

  for i in range(len(sequence)):
    if not sequence[i]:
      if i + K > len(S):
        return 'IMPOSSIBLE'
      else:
        #Flip
        for j in range(K):
          sequence[i+j] = not sequence[i+j]
        result += 1

  return str(result)

def main():
  T = int(input())
  for t in range(1, T +1):
    S, K = input().split(' ')
    result = solution(S, int(K))
    print('Case #{}: {}'.format(t, result))

if __name__ == '__main__':
  main()
