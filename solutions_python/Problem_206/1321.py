T = int(input())
for i in range(T):
  DN = input().split()
  D = int(DN[0])
  N = int(DN[1])
  horses = []
  j = 1
  horse = input().split()
  horse = [int(n) for n in horse]
  slowestTime = (D - horse[0]) / horse[1]
  while j < N:
    horse = input().split()
    horse = [int(n) for n in horse]
    slowestTime = max((D - horse[0]) / horse[1], slowestTime)
    j += 1
  v = D / slowestTime
  print("Case #", end = "")
  print(i + 1, end = ": ")
  print(v)
    