f = open('B-large.in')
o = open('output.txt', 'w')
n = int(f.readline())
for i in range(n):
  diners = int(f.readline().strip())
  q = [int(x) for x in f.readline().strip().split(" ")]
  counts = [0] * (max(q)+1)
  for x in q:
    counts[x] += 1
  q_max = len(counts)-1
  t_min = q_max
  for j in range(1, q_max+1):
    t = 0
    for n in range(1, len(counts)):
      t += counts[n] * ((n-1)/j)
      if t >= t_min:
        break
    t_min = min(t_min, t+j)
  #print counts, t_min
  o.write("Case #"+str(i+1)+": "+str(t_min)+"\n")
f.close()
o.close()