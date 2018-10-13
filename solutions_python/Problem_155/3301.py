file = "large.in"

with open(file) as handle:
  T = int(handle.readline())

  for i in range(T):
    Smax, S = handle.readline().split()
    Smax = int(Smax)

    without_friends = 0
    with_friends = 0

    for shyness, digit in enumerate(S):
      count = int(digit)
      if not count: continue
      if shyness > with_friends:
        with_friends += shyness - with_friends
      without_friends += count
      with_friends += count

    print "Case #{}: {}".format(i + 1, with_friends - without_friends)

