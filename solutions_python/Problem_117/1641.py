from copy import deepcopy
def parse_input(infile):
  next(infile)
  testno = 0
  while True:
    line = next(infile)
    N, M = map(int, line.split())
    test = []
    for i in range(N):
      line = next(infile)
      test.append([int(i) for i in line.split()])
    testno += 1
    yield testno, N, M, test

def is_valid(N, M, test):
  """
  Take each height at a time
  and see if a horizontal/vertical line can be made
  through all cells with that height.
  If so, this is a valid final step in the mowing pattern
  so un-mow those cells and continue with the next highest height,
  until we've covered the entire strategy in reverse.
  If at any point we can't make a horizontal/vertical line, then
  we have an "island" - a cell we can't create without destroying
  the surrounding area.
  """
  copy = deepcopy(test)
  for height in range(1, 101):
    for n in range(N):
      for m in range(M):
        cell = test[n][m]
        if cell == height:
          copy[n][m] += 1

          vertical = [row[m] for row in test]
          horizontal = test[n]
          if any((cell > height for cell in vertical)) and \
                any((cell > height for cell in horizontal)):
              return 'NO'
    test = copy
    copy = deepcopy(test)
  return 'YES'

if __name__ == '__main__':
  import sys
  for testno, N, M, arr in parse_input(sys.stdin):
    print('Case #{0}: {1}'.format(testno, is_valid(N, M, arr)))
