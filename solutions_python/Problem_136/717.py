f = open("output.txt","w")
t = int(raw_input())
for i in range(0,t):
  f.write("Case #"+str(i+1)+": ")
  arr = list(map(float,raw_input().split()))
  C = arr[0]
  F = arr[1]
  X = arr[2]
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
    