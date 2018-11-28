from sys import stdin

def check(N,K):
  for x in xrange(len(N)):
    if N[x] < K[x]:
      return False
  return True

Q = int(stdin.readline())
for qq in xrange(Q):
  stdin.readline()
  N = sorted(map(float, stdin.readline().split()))
  K = sorted(map(float, stdin.readline().split()))
  uN = [False for x in xrange(len(N))]
  uK = [False for x in xrange(len(N))]
  normal_pts = 0
  for x in xrange(len(N)):
    uN[x] = True
    play = N[x]
    answer = None
    backup = None
    for idx,can in enumerate(K):
      if not uK[idx]:
        if K[idx] > play:
          answer = idx
          uK[idx] = True
          break
        if backup is None:
          backup = idx
    if answer is None:
      answer = backup
      normal_pts += 1
  while not check(N,K):
    N=N[1::]
    K=K[:-1:]
  cheat_pts = len(N)
  print("Case #"+str(qq+1)+": "+str(cheat_pts)+" "+str(normal_pts))