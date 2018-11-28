with open("A-large.in", "r") as f:
  tc = 1

  for line in f.readlines()[1:]:
    shy_max, people = line.split()
    shy_max = int(shy_max)    
    people = [int(x) for x in people]

    curr_sum = 0
    cumulativePeople = [0]
    for shy_level in people[:-1]:
      curr_sum += shy_level
      cumulativePeople.append(curr_sum)

    people_needed = 0
    index = 0
    for cumul in cumulativePeople:
      if cumul + people_needed < index:
        people_needed += (index - cumul - people_needed)
      index += 1

    print "Case #{}: {}".format(tc, people_needed)
    tc += 1

