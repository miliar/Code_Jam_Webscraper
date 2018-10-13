#!/usr/bin/env python

def solve():
  first_answer = int(raw_input())
  first_arrangement = []
  for i in xrange(4):
    first_arrangement.append(map(lambda x: int(x), raw_input().split()))
  second_answer = int(raw_input())
  second_arrangement = []
  for i in xrange(4):
    second_arrangement.append(map(lambda x: int(x), raw_input().split()))

  first = sorted(first_arrangement[first_answer - 1])
  second = sorted(second_arrangement[second_answer - 1])

  i, j = 0, 0
  meet = []
  while i < 4 and j < 4:
    if first[i] == second[j]:
      meet.append(first[i])
      i = i + 1
      j = j + 1
    elif first[i] < second[j]:
      i = i + 1
    else:
      j = j + 1

  if len(meet) == 0:
    return 'Volunteer cheated!'
  elif len(meet) == 1:
    return str(meet[0])
  else:
    return 'Bad magician!'


def main():
  n = int(raw_input())
  for i in xrange(n):
    print 'Case #%d: %s' % (i+1, solve())

if __name__ == '__main__':
  main()
