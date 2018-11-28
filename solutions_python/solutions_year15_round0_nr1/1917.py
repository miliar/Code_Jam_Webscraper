t = int(input())

for i in range(1, t + 1):
  smax, ks = input().split(" ")
  smax = int(smax)
  ks = [int(k) for k in ks]

  added = 0
  currently_standing = 0
  for (k, num_shy) in enumerate(ks):
    if currently_standing < k and num_shy > 0:
      added += k - currently_standing
      currently_standing = k
    currently_standing += num_shy

  print("Case #{:d}: {:d}".format(i, added))
