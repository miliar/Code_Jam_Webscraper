import re
import numpy

tokens = [float(x) for x in re.split('\s+', file('B-large.in').read()) if x != '']
t = tokens.__iter__()
num_instances = int(t.next())
for ii in range(0, num_instances):
  C = t.next()
  F = t.next()
  X = t.next()
  rate = 2.0
  farm_time = 0.0
  time_needed = farm_time + X / rate
  while True:
    new_rate = rate + F
    new_farm_time = C / rate + farm_time
    new_time_needed = new_farm_time + X / new_rate
    # print (new_rate, new_bias, new_time_needed)
    if new_time_needed >= time_needed:
      break
    time_needed = new_time_needed
    rate = new_rate
    farm_time = new_farm_time
  print 'Case #%d: %.9f' % (ii + 1, time_needed)
