




readfile = open("C-small-attempt1.in")
writefile = open("output3.txt", "w")

lines = readfile.readlines()
#assert int(lines[0]) == len(lines) - 1

flag = 0
prob_num = 0
for line_num in xrange(1,len(lines)):
  line = lines[line_num]
  if flag == 0:
    n,q = line.split()
    print line, n, q
    n = int(n)
    q = int(q)
    flag = 1
    horses = []
    routes = []
    deliveries = []
    prob_num += 1
  elif flag <= n:
    e, s = line.split()
    e = int(e)
    s = int(s)
    horses.append([e,s])
    flag += 1
  elif flag <= 2*n:
    routes.append([int(x) for x in line.split()])
    flag += 1
  elif flag <= 2*n+q:
    deliveries.append([int(x) for x in line.split()])
    print deliveries
    print routes
    print horses
    flag = 0
    best_times = [0] * n
    for i in xrange(n-1):
      best_time = 2**50
      distance = 0.
      time = 0.
      e, s = horses[n-2-i]
      for j in xrange(i+1):
        distance += routes[n-2-i+j][n-2-i+j+1]
        #print distance, e
        if distance <= e:
          time = best_times[n-2-i+j+1] + distance / s
          if time < best_time:
            best_time = time
      best_times[n-2-i] = best_time
    writefile.write("Case #%d: %s\n" % (prob_num, best_times[0]))

writefile.close()