#! /usr/bin/env python
# code.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2012 Apr 14

import sys

scores={30: [[10,10,10],[-1,-1,-1]],
        29: [[10,10, 9],[-1,-1,-1]],
        28: [[10, 9, 9],[10,10, 8]],
        27: [[ 9, 9, 9],[10, 9, 8]],
        26: [[ 9, 9, 8],[10, 8, 8]],
        25: [[ 9, 8, 8],[ 9, 9, 7]],
        24: [[ 8, 8, 8],[ 9, 8, 7]],
        23: [[ 8, 8, 7],[ 9, 7, 7]],
        22: [[ 8, 7, 7],[ 8, 8, 6]],
        21: [[ 7, 7, 7],[ 8, 7, 6]],
        20: [[ 7, 7, 6],[ 8, 6, 6]],
        19: [[ 7, 6, 6],[ 7, 7, 5]],
        18: [[ 6, 6, 6],[ 7, 6, 5]],
        17: [[ 6, 6, 5],[ 7, 5, 5]],
        16: [[ 6, 5, 5],[ 6, 6, 4]],
        15: [[ 5, 5, 5],[ 6, 5, 4]],
        14: [[ 5, 5, 4],[ 6, 4, 4]],
        13: [[ 5, 4, 4],[ 5, 5, 3]],
        12: [[ 4, 4, 4],[ 5, 4, 3]],
        11: [[ 4, 4, 3],[ 5, 3, 3]],
        10: [[ 4, 3, 3],[ 4, 4, 2]],
        9:  [[ 3, 3, 3],[ 4, 3, 2]],
        8:  [[ 3, 3, 2],[ 4, 2, 2]],
        7:  [[ 3, 2, 2],[ 3, 3, 1]],
        6:  [[ 2, 2, 2],[ 3, 2, 1]],
        5:  [[ 2, 2, 1],[ 3, 1, 1]],
        4:  [[ 2, 1, 1],[ 2, 2, 0]],
        3:  [[ 1, 1, 1],[ 2, 1, 0]],
        2:  [[ 1, 1, 0],[ 2, 0, 0]],
        1:  [[ 1, 0, 0],[-1,-1,-1]],
        0:  [[ 0, 0, 0],[-1,-1,-1]]}

def main():
  file = open(sys.argv[1])
  nb_cases = int(file.readline())
  nb_case = 1
  for i in range(nb_cases):
    numbers = file.readline().split(' ')
    N = int(numbers[0])
    S = int(numbers[1])
    p = int(numbers[2])
    responses = 0
    for n in range(N):
      score = int(numbers[2+n+1])
      p_scores=scores[score]
      found = 0
      for s in p_scores[0]:
        if s >= p:
          responses = responses + 1
          found = 1
          break
      if found == 0 and S > 0:
        for s in p_scores[1]:
          if s >= p:
            responses = responses + 1
            S = S - 1
            break
    sys.stdout.write(("Case #%d: %d\n" % (nb_case, responses) ))
    nb_case += 1
    file.close

if __name__ == "__main__":
  main()

