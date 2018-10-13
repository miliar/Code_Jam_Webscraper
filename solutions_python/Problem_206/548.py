def maximumSpeed(D, positions, speeds):
  latestTime = 0
  for horse in xrange(len(positions)):
    latestTime = max(latestTime, float(D - positions[horse]) / speeds[horse])
  return float(D) / latestTime

with open('../inputs/A-large.in') as infile:
  with open('../outputs/A-large.out', 'wb') as outfile:
    cases = int(infile.readline())
    for i in xrange(cases):
      [D, N] = map(int, infile.readline().strip().split(' '))
      positions = []
      speeds = []
      for _ in xrange(N):
        [x, v] = map(int, infile.readline().strip().split(' '))
        positions.append(x)
        speeds.append(v)
      outfile.write('Case #' + str(i + 1) + ': ')
      outfile.write(str(maximumSpeed(D, positions, speeds)))
      outfile.write('\n')
