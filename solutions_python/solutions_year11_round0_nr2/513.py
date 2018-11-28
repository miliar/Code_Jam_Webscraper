#!/usr/bin/env python

import sys

def main():
  T = int(sys.stdin.readline())
  for test in range(1, T + 1):
    line = sys.stdin.readline().split()
    combine = {}
    destroy = {}

    C = int(line[0])
    pair_combine = line[1 : C + 1]
    for pair in pair_combine:
      combine[pair[0:2]] = pair[2]
      combine[pair[1::-1]] = pair[2]

    D = int(line[C + 1])
    pair_destroy = line[C + 2 : C + D + 2]
    for pair in pair_destroy:
      if pair[0] not in destroy:
        destroy[pair[0]] = set()
      if pair[1] not in destroy:
        destroy[pair[1]] = set()

      destroy[pair[0]].add(pair[1])
      destroy[pair[1]].add(pair[0])
    
    N = int(line[C + D + 2])
    string = line[C + D + 3]

    st = []
    for i in range(N):
      st.append(string[i])
      done = False
      while not done and len(st) > 1:
        done = True
        if st[-2] + st[-1] in combine:
          st[-2] = combine[st[-2] + st[-1]]
          st.pop(len(st) - 1)
          done = False
        if st[-1] in destroy and destroy[st[-1]].intersection(set(st[:-1])):
          st = []
          done = False

    print "Case #%d: [%s]" % (test, ", ".join(st))

  return 0

if __name__ == "__main__":
  main()

