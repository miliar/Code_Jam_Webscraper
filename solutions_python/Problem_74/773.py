import sys

def line(): return sys.stdin.readline().strip('\n')

n = int(line())

for case in range(1, n+1):
  tmp = line().split(" ")[1:]
  pos = {'O': 1, 'B': 1}
  seq = []
  time = 0
  freeTime = 0
  for i in range(0, len(tmp)/2):
    who = tmp[i*2]
    button = int(tmp[i*2+1])
    seq.append((who, button))
  prevWho = 'x'
  for (who, button) in seq:
    tNeeded = abs(pos[who] - button) + 1
    pos[who] = button
    if prevWho == who:
      freeTime += tNeeded
    else:
      tNeeded = max(1, tNeeded - freeTime)
      freeTime = tNeeded
      prevWho = who
    time += tNeeded
  print "Case #" + str(case) + ": " + str(time)
