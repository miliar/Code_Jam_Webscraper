def testcase(t, data):
  pos = [1, 1]
  seconds = [0, 0]
  N = int(data[0])
  for i in xrange(1, N * 2 + 1, 2):
    R = data[i]
    P = int(data[i + 1])
    if R == 'O':
      robot = 0
    else:
      robot = 1
    # move to button
    seconds[robot] += abs(P - pos[robot])
    pos[robot] = P
    # wait for other robot
    if seconds[robot] < seconds[1 - robot]:
      seconds[robot] = seconds[1 - robot]
    # press button
    seconds[robot] += 1
  print 'Case #%d: %d' % (t, max(seconds[0], seconds[1]))

T = int(raw_input())
for t in xrange(1, T + 1):
  testcase(t, raw_input().split())