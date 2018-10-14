with open("B-large.in", "r") as f:
  tc = 1

  lines = f.readlines()
  i = 1

  while i < len(lines):
    D = lines[i].strip()
    plates = [int(x) for x in lines[i + 1].strip().split()]
    i += 2
  
    min_minutes = max(plates)
    trial = 2

    while trial < min_minutes:
      # See if we can divide the stacks of pancakes into 'trial' sized blocks. Then it will take trial minutes
      # plus however many it takes to divide the chunks into 'trial' sized blocks ( (p-1) // trial ).
      min_minutes = min(min_minutes, sum([(p-1) // trial for p in plates]) + trial)
      trial += 1

    print "Case #{}: {}".format(tc, min_minutes)
    tc += 1

