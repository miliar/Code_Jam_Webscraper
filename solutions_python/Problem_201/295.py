t = int(raw_input())
for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]
  t = {n : 1};
  l = 0;
  r = 0;
  while (k > 0):
    key = max(t);
    k = k - t[key];
    if (key % 2 == 1):
        l = key / 2
        r = key / 2
        if key/2 in t:
            t[key/2] = t[key/2] + 2 * t[key]
        else:
            t[key/2] = 2 * t[key]
    else:
        l = key / 2 - 1
        r = key / 2
        if key/2 in t:
            t[key/2] = t[key/2] + t[key]
        else:
            t[key/2] = t[key]

        if (key/2 -1) in t:
            t[key/2 - 1] = t[key/2 - 1] + t[key]
        else:
            t[key/2 - 1] = t[key]
    del t[key]

  print "Case #{}: {} {}".format(i, r, l)
