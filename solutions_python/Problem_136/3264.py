from __future__ import division

import sys, os

base_rate = 2.0
def do_case(farm_cost, farm_add, goal):
  done = False
  time = 0.0
  cookies = 0
  num_farms = 0
  skipped_buying = False
  
  while not done:
    rate = base_rate + num_farms * farm_add
	
	
    #time_step = max(min( (farm_cost - cookies) / rate, (goal - cookies) / rate  ), 10**-5)
    time_step = min( (farm_cost - cookies) / rate, (goal - cookies) / rate  )
    time += time_step
    cookies += rate*time_step
    #print "timestep step:%f, time: %f cookies: %f farms:%d " % ( time_step, time, cookies, num_farms)
    
    left_buy = (goal - (cookies - farm_cost)) / (rate + farm_add)
    left_not = (goal - cookies) / (rate)
	
    #print left_buy, left_not, goal - cookies
    if cookies - goal >= (-1 * 10**-7):
      return time
    if left_buy > 0 and left_buy < left_not and cookies - farm_cost >= -1 * 10**-7:
       cookies -= farm_cost
       num_farms += 1
       #print cookies, num_farms, time, 'bought farm'
    else:
      #print 'didnt buy a farm'	
      return time + (goal - cookies) / rate
      #print cookies, num_farms, time, 'not farm'

f = open(sys.argv[1], 'r')
out = open(sys.argv[2], 'w')

num_cases = int(f.readline())
for i in range(1,num_cases+1):
	a,b,c  = map(float, f.readline().split())
	#print "case: %d, farm_cost: %f, farm_add: %f, goal: %f"% (i, a, b,c)
	res = do_case(a,b,c)
	print "Case #%d:" % (i), res
	out.write("Case #%d: %s\n" % (i, res))

	
	