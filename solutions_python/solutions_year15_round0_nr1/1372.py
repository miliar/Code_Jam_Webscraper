for i in range(int(raw_input())):
  s = raw_input()

  total = 0
  needed = 0
  for j, c in enumerate(s.split()[1]):
    if int(c) == 0:
        continue

    if total >= j:
        #print("total: %d" % (total))
        total += int(c)
    else:
        #print("total: %d, needed: %d" % (total, j-total))
        needed += j-total
        total += int(c) + (j-total)
  print('Case #%d: %d'%(i+1,needed))
