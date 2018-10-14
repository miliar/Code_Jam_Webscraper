def read_file(input):
  my_list = []
  test_case = []
  case = []
  file = open(input, 'r')
  for line in file:
    my_list.append(line.rstrip('\n').split(',')[0].split())
  my_list.pop(0)
  return my_list

def cookie_cutter(cases):
  counter = 0
  f = open('output.txt','w')
  for case in cases:
    counter += 1
    cookie_inc = 2
    farm_cost = float(case[0])*1.000000
    farm_bonus = float(case[1])*1.000000
    goal = float(case[2])*1.000000

    #Time for farm 
    farmttl = farm_cost/cookie_inc
    #Time for goal
    goalttl = goal/cookie_inc
    # Time for next farm with increment
    next_farmttl = farm_cost/(farm_bonus + cookie_inc)
    # Time for goal with increment
    next_goalttl = goal/(farm_bonus + cookie_inc)

    total_time = 0

    def buy_farm(cookie_inc, farm_bonus):
      return cookie_inc + farm_bonus

    while goalttl > (farmttl + next_goalttl):

        cookie_inc = buy_farm(cookie_inc, farm_bonus)
        total_time = total_time + farmttl

        farmttl = farm_cost/cookie_inc
        #Time for goal
        goalttl = goal/cookie_inc
        # Time for next farm with increment
        next_farmttl = farm_cost/(farm_bonus + cookie_inc)
        # Time for goal with increment
        next_goalttl = goal/(farm_bonus + cookie_inc)

    
    f.write( 'Case #%s: %0.7f\n' % (counter,total_time+goalttl))



if __name__ == "__main__":
  cases = read_file('B-large.in')
  cookie_cutter(cases)
