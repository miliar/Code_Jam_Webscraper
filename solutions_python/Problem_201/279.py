def bathroom(N, K):
  intervalCounts = {}
  intervalCounts[N] = 1
  while True:
    currentLargest = max(intervalCounts)
    if intervalCounts[currentLargest] >= K:
      return (currentLargest / 2, (currentLargest - 1) / 2)
    else:
      count = intervalCounts[currentLargest]
      del intervalCounts[currentLargest]
      intervalCounts[currentLargest / 2] = intervalCounts.get(currentLargest / 2, 0) + count
      intervalCounts[(currentLargest - 1) / 2] = intervalCounts.get((currentLargest - 1) / 2, 0) + count
      K -= count

with open('../inputs/C-large.in') as infile:
  with open('../outputs/C-large.out', 'wb') as outfile:
    cases = int(infile.readline())
    for i in xrange(cases):
      [N, K] = map(int, infile.readline().strip().split(' '))
      (x, y) = bathroom(N, K)
      outfile.write('Case #' + str(i + 1) + ': ')
      outfile.write(str(x) + ' ' + str(y))
      outfile.write('\n')
