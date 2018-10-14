import sys
def Gcd(a,b):
  while a and b:
    a %= b
    if a:
      b %= a
  return a+b

for case_num in range(int(sys.stdin.readline())):
  events = [long(sec) for sec in sys.stdin.readline().split()]
  events.remove(events[0])
  events.sort()
  last = events[0]
  events = [events[i+1]-events[i] for i in range(len(events)-1)]
  factor = events[0]
  for event in events:
    factor = Gcd(factor,event)
  print 'Case #' + str(case_num + 1) + ': ' + str((factor - (last % factor)) % factor)
