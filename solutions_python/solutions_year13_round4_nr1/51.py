def cost(n_stops, distance):
  return distance*n_stops - distance*(distance-1)/2

def cost_without_swaps(n_stops, trips):
  s = 0
  for start,end,n in trips:
    s += n*cost(n_stops, end-start)
  return s

def cost_with_swaps(n_stops, trips):
  starts = [0]*n_stops
  stops  = [0]*n_stops
  for a,b,n in trips:
    starts[a-1] += n
    stops[b-1] += n
  s = 0
  for i in range(n_stops):
    j = i
    while stops[i]:
      m = min(stops[i],starts[j])
      s += m*cost(n_stops, i-j)
      stops[i] -= m
      starts[j] -= m
      if starts[j] == 0:
        j -= 1
  return s
  
  
def solve():
  n_stops, n_trips = map(int,raw_input().split())
  trips = [map(int,raw_input().split()) for i in range(n_trips)]
  return cost_without_swaps(n_stops, trips) - cost_with_swaps(n_stops, trips)
  

n_cases = input()
for case in range(1,n_cases+1):
  print 'Case #%d: %s' % (case, str(solve()))