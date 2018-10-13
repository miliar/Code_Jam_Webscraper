f = open("output.txt","w")
t = int(raw_input())
for i in range(0,t):
  f.write("Case #"+str(i+1)+": ")
  array = list(map(float,raw_input().split()))
  C = array[0]
  F = array[1]
  X = array[2]
  CR = 2
  cost_inc_rate = C/CR
  prev_cost = X/CR
  total_cost = cost_inc_rate + X/(CR+F)
  while prev_cost >= total_cost:
    prev_cost = total_cost
    CR += F
    cost_inc_rate += C/CR
    total_cost = cost_inc_rate + X/(CR+F)
  print "%.7f" %prev_cost
  f.write("%.7f\n" % prev_cost )
f.close()
    