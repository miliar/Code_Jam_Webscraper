ncase = int(raw_input())
for nt in range(1, ncase+1):
  kandidat = []
  for i in range(2):
    nrow = int(raw_input()) - 1
    for k in range(4):
      rows = map(int, raw_input().strip().split())
      if nrow == k:
        kandidat.append(rows[:])

  ans = []
  for x in kandidat[0]:
    if x in kandidat[1]: ans.append(x)

  nans = len(ans)
  print "Case #" + str(nt) + ":",
  if nans == 0: print "Volunteer cheated!"
  elif nans == 1: print ans[0]
  else: print "Bad magician!"
