
class Horse:
  def __init__(self, distance, max_speed):
    self.distance = distance
    self.max_speed = max_speed
    self.time = distance / max_speed
    self.adjusted_speed =  self.max_speed
    self.newtime = self.time

  def __str__(self):
    return self.location + " " + self.max_speed + " " + self.time


def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{:.7f}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


t = int(raw_input())
for i in xrange(1, t + 1):
  total_distance, no_of_horses = [int(s) for s in raw_input().split(" ")]
  horses = []
  for k in xrange(0, no_of_horses):
    location, max_speed = [float(s) for s in raw_input().split(" ")]
    horses.append( Horse(total_distance - location, max_speed))

  horses.sort(key=lambda x: x.distance, reverse=True)

  for j in xrange(1, len(horses)):
    if horses[j].time < horses[j-1].time:
      horses[j].newtime = horses[j-1].time
      horses[j].adjusted_speed = horses[j].distance / horses[j].newtime

  print "Case #{}: {}".format(i, truncate(total_distance / horses[-1].newtime, 6) )
#  print "Case #{}: {:.6f}".format(i, total_distance / horses[-1].newtime )

