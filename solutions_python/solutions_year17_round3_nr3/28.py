def optimalProbability(N, K, U, P):
  sortedProbabilities  = sorted(P + [1.0])
  # Try assigning first to lowest.
  if N == K:
    index = 0
    currentProbability = sortedProbabilities[index]
    nextProbability    = sortedProbabilities[index + 1]
    while U >= 0:
      necessaryUnits     = (index + 1) * (nextProbability - currentProbability)
      if necessaryUnits > U:
        currentProbability += U / (index + 1)
        break
      else:
        U     -= necessaryUnits
        index += 1
        currentProbability = sortedProbabilities[index]
        if index == N:
          break
        nextProbability    = sortedProbabilities[index + 1]
    result = 1
    for i in xrange(index + 1):
      result *= currentProbability
    for i in xrange(index + 1, N):
      result *= sortedProbabilities[i]
    return result
  return 0

with open('../inputs/C-small-1-attempt0.in') as infile:
  with open('../outputs/C-small-1-attempt0.out', 'wb') as outfile:
    cases = int(infile.readline())
    for i in xrange(cases):
      [N, K] = map(int, infile.readline().split(' '))
      U = float(infile.readline())
      P = map(float, infile.readline().split(' '))
      outfile.write('Case #' + str(i + 1) + ': ')
      outfile.write('%.6f' % optimalProbability(N, K, U, P))
      outfile.write('\n')
