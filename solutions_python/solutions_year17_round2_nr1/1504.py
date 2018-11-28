import sys

def solve(d, n):
  steeds = []
  for i in range(n):
    k, s = map(int,sys.stdin.readline().split())
    steeds.append((k, s))
  steeds.sort()
  steeds.reverse()
  hours = []
  for i, (k, s) in enumerate(steeds):
    if i == 0:
      time = (d - k) / float(s)
      prev = (k, s, time)
      hours.append(prev)
    else:
      if s <= prev[1]:
        time = (d - k) / float(s)
        prev = (k, s, time)
        hours.append(prev)
      else:
        timeToNext = (prev[0] - k) / float(s - prev[1])
        timeToGoal = (d - k) / float(s) 
        if timeToNext < timeToGoal:
          prev = (k, s, prev[2])
        else:
          prev = (k, s, timeToGoal)
        hours.append(prev)
  slowest = hours[0][2] 
  for (_, _, t) in hours:
    slowest = max(t, slowest)
  return d / slowest
    
        

if __name__ == '__main__':
  tests = input()
  for i in range(tests):
    x,y = map(int,sys.stdin.readline().split())
    res = solve(x,y)
    print "Case #" + str(i + 1) +": " + ('%.6f' % res)

      

