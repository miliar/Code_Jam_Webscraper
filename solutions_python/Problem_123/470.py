for T in range(1, int(input())+1):
  A, N = input().split()
  A, N = int(A), int(N)
  motes = []
  a = []
  for m in input().split():
    motes.append(int(m))
  motes.sort()
  
  # absorb as many as possible
  while len(motes) > 0 and A > motes[0]:
    A += motes.pop(0)

  maxtime = len(motes)
  addtime = 1
  bA, bmotes = int(A), list(motes)
  while addtime < maxtime:
    A, motes = int(bA), list(bmotes)
    for i in range(addtime):
      A += A - 1	# add one
      while len(motes) > 0 and A > motes[0]:
        A += motes.pop(0)
    if addtime + len(motes) < maxtime:
      maxtime = addtime + len(motes)
    addtime += 1
  print("Case #%d: %d" % (T, maxtime))
