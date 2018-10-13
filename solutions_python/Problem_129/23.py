from heapq import *

T = int(raw_input())

MOD = 1000002013

def cost(df, N):
  return df*N - (df*df - df)/2

for test in range(T):
  N, M = map(int,raw_input().split())
  h = []
  totcost = 0
  for p in range(M):
    e, o, pp = map(long,raw_input().split())
    heappush(h, (e, -1, pp))
    heappush(h, (o, 1, pp))
    totcost = totcost + cost(o - e, N) * pp
  redcost = 0
  tickets = []
  while h != []:
    station, inout, pp = heappop(h)
    if inout == -1: #people entering
      heappush(tickets, (-station, pp))
    else: #people going out
      while pp > 0:
        ticket, num = heappop(tickets)
        ticket = -ticket
        if num > pp:
          redcost = redcost + cost(station - ticket, N) * pp
          heappush(tickets, (-ticket, num-pp))
          pp = 0
        else:
          redcost = redcost + cost(station - ticket, N) * num
          pp = pp - num
  print 'Case #' + str(test+1) + ':', (totcost - redcost) % MOD
  