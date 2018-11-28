import math

def solve(MAX):
  fasq = []
  st = 1
  v = 1
  while v < MAX:
    ss = str(st)
    v = int(ss + ss[::-1]) ** 2
    sv = str(v)
    if v <= MAX:
      if sv == sv[::-1]:
        fasq.append(v)
    v = int(ss + ss[-2::-1]) ** 2
    sv = str(v)
    if v <= MAX:
      if sv == sv[::-1]:
        fasq.append(v)
    st = st + 1
  
  return fasq
  
T = int(raw_input())

fasq = solve(10**15)

for case in range(1,T+1):
  A, B = map(int,raw_input().split())
  count = 0
  print 'Case #' + str(case) + ': ' + str(len([f for f in fasq if f >= A and f <= B])) 