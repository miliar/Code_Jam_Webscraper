#! /usr/bin/env python2

def main():
  num_tests = int(raw_input())
  for test in range(num_tests):
    rows = []
    for _ in range(2):
      drop_num = int(raw_input()) - 1
      for _ in range(drop_num):
        raw_input()
      row = [int(elem) for elem in raw_input().split()]
      rows.append(row)
      for _ in range(4 - drop_num - 1):
        raw_input()  # flush rest of field
    candidates = []
    for cand in rows[0]:
      if cand in rows[1]:
        candidates.append(cand)
    if not candidates:
      verdict = 'Volunteer cheated!'
    elif len(candidates) > 1:
      verdict = 'Bad magician!'
    else:
      verdict = str(candidates[0])
    print 'Case #%i: %s' % (test + 1, verdict)

if __name__ == '__main__':
  main()
