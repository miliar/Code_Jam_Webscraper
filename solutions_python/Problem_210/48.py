file_in = open('B-large.in', 'r')
file_out = open('b.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  ac, aj = map(int, file_in.readline().split())

  ring = [" "] * 1440

  ctotal = 0

  for i in range(ac):
    start, end = map(int, file_in.readline().split())
    for i in range(start, end):
      ring[i] = 'C'
    ctotal += end - start

  for i in range(aj):
    start, end = map(int, file_in.readline().split())
    for i in range(start, end):
      ring[i] = 'J'

  positive = []
  neutral = []
  negative = []

  # find the last non-neutral space.
  endpoint = None
  for i in range(1440):
    if(ring[i] != ' '):
      endpoint = i

  print("".join(ring))
  print("endpoint: ", endpoint)
  left = endpoint

  csections = 0
  cstart = False

  for i in range(1, 1441):
    it = endpoint + i
    if it >= 1440:
      it -= 1440
    if ring[it] == 'C' and cstart is False:
      cstart = True
    if ring[it] != 'C' and cstart is True:
      csections += 1
      cstart = False

    if ring[it] != ' ':
      if(it - left != 1):
        diff = it - left - 1
        while(diff < 0):
          diff += 1440
        if ring[left] != ring[it]:
          neutral.append(diff)
        elif ring[left] == 'C':
          positive.append(diff)
        elif ring[left] == 'J':
          negative.append(diff)
      left = it
      size = 0
    it += 1
    if it >= 1440:
      it = 0
  if cstart is True:
    csections += 1

  print("ctotal", ctotal)
  print("csections", csections)
  print("Positive", positive)
  print("Neutral", neutral)
  print("Negative", negative)

  # First, take as many out of the positive list as possible.
  positive.sort()
  negative.sort(reverse=True)
  while len(positive) > 0 and ctotal + positive[0] <= 720:
    ctotal += positive.pop(0)
    csections -= 1

  # Next take all the neutral sections
  ctotal += sum(neutral)

  while ctotal < 720 and len(negative) > 0:
    ctotal += negative.pop(0)
    csections += 1

  ans = csections * 2
  file_out.write("Case #{}: {}\n".format(t, ans))