# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def pony_express(N, city_specs, distance_specs, to_investigate):
  time_matrix = [[-float('inf')] * N] * N
  # small case
  possible_routes = []
  for i in xrange(N):
    possible_routes.append([])
  # possible_route[x]: collections of (time, horse_speed, horse_remain)
  possible_routes[1] = [(distance_specs[0][1] / city_specs[0][1], city_specs[0][1], city_specs[0][0] - distance_specs[0][1])]

  for i in xrange(1, N-1):
    for possible_route in possible_routes[i]:
      current_time, horse_speed, horse_remain = possible_route  
      city_horse_remain, city_horse_speed = city_specs[i]
      if city_horse_speed >= horse_speed and city_horse_remain >= horse_remain:
        possible_routes[i+1].append((current_time + distance_specs[i][i+1] / city_horse_speed, city_horse_speed, city_horse_remain -  distance_specs[i][i+1]))
      elif city_horse_speed <= horse_speed and city_horse_remain <= horse_remain:
        possible_routes[i+1].append((current_time + distance_specs[i][i+1] / horse_speed, horse_speed, horse_remain -  distance_specs[i][i+1]))
      else:
        if horse_remain >= distance_specs[i][i+1]:
          possible_routes[i+1].append((current_time + distance_specs[i][i+1] / horse_speed, horse_speed, horse_remain -  distance_specs[i][i+1]))

        if city_horse_remain >= distance_specs[i][i+1]:
          possible_routes[i+1].append((current_time + distance_specs[i][i+1] / city_horse_speed, city_horse_speed, city_horse_remain -  distance_specs[i][i+1]))

  result = float('inf')
  # print possible_routes
  for possible_route in possible_routes[N-1]:
    if result > possible_route[0]:
      result = possible_route[0]
  return [result]







t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N, Q = [int(s) for s in raw_input().split(" ")]
  city_specs = []
  for j in xrange(N):
    E,S = [float(s) for s in raw_input().split(" ")]
    city_specs.append((E,S))
  distance_specs = []
  for j in xrange(N):
    distance_spec = [float(s) for s in raw_input().split(" ")]
    distance_specs.append(distance_spec)
  to_investigate = []
  for j in xrange(Q):
    U, V = [int(s) for s in raw_input().split(" ")]
    to_investigate.append((U,V))

  answers = pony_express(N, city_specs, distance_specs, to_investigate)
  to_print = ''
  for j in answers:
    to_print += ' ' + str(j)
  print "Case #{}: {}".format(i, to_print)

 # check out .format's specification for more formatting options