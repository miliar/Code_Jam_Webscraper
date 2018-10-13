for tc in range(input()):
  d, n = raw_input().split(" ")
  max_time = 0.0
  for i in range(int(n)):
    pos, spe = raw_input().split(" ")
    distance_to_go = float(d) - float(pos)
    time = distance_to_go / float(spe)
    if max_time < time:
      max_time = time
  cruise_speed = float(d) / float(max_time)
  print "Case #%s: %s" % (tc + 1, cruise_speed)