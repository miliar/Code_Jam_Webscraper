#!/usr/bin/env python
import sys

def main():
  T = int(sys.stdin.readline().strip())
  for case in range(1, T + 1):
    N = int(sys.stdin.readline().strip())

    pos = [0.0, 0.0, 0.0]
    vec = [0.0, 0.0, 0.0]
    for n in range(N):
      numbers = map(float, sys.stdin.readline().strip().split(' '))
      p = numbers[:3]
      v = numbers[3:]
      for i in range(3):
        pos[i] += p[i]
        vec[i] += v[i]

    for i in range(3):
      pos[i] /= N
      vec[i] /= N

    up = 0.0
    bot = 0.0
    for i in range(3):
      up += pos[i] * vec[i]
      bot += vec[i] * vec[i]
    if bot == 0:
      t = 0
    else:
      t = - up / bot

    if t < 0:
      t = 0

    d = 0.0
    for i in range(3):
      d += (pos[i] + vec[i] * t) ** 2.0
    d = d ** (0.5)


    print 'Case #' + str(case) + ': %.8f %.8f' % (d, t)


if __name__ == '__main__':
  main()
