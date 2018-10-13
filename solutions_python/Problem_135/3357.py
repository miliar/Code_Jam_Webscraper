#!/usr/bin/env python3
import fileinput

def solve(f):

  first_answer = int(next(f))
  for _ in range(first_answer - 1): next(f)
  first_set = set(next(f).split())
  for _ in range(4 - first_answer): next(f)

  second_answer = int(next(f))
  for _ in range(second_answer - 1): next(f)
  second_set = set(next(f).split())
  for _ in range(4 - second_answer): next(f)

  common = first_set & second_set
  if len(common) == 1:
    return common.pop()
  elif len(common) == 0:
    return "Volunteer cheated!"
  else:
    return "Bad magician!"


if __name__ == '__main__':
  with fileinput.input() as f:
    tests = int(next(f))
    for t in range(1, tests + 1):
      answer = solve(f)
      print("Case #{t}: {answer}".format(t=t, answer=answer))
