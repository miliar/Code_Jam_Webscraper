t = int(raw_input())

for i in range(t):
  s = raw_input()
  s = s.split()

  max_shy = int(s[0])

  temp = list(s[1])

  for j in range(max_shy+1):
    temp[j] = int(temp[j])

  current_standing = 0
  n_friends_added = 0

  for j in range(max_shy + 1):
    x = 0
    if j >  current_standing and temp[j] > 0:
      x = j - current_standing
      n_friends_added = n_friends_added + x

    current_standing = current_standing + temp[j] + x

    # print j, x, current_standing, n_friends_added

  print "Case #%d: %d"%(i+1, n_friends_added)
