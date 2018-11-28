import sys

def process_case(line):

  C, F, X = map(float, line.split())
  prod_rate = 2.0
  total_time = 0.0
  done = False
  while  done == False:
    next_farm_time    = (C/float(prod_rate)) + X/float(prod_rate+F)          # time_till_next_farm(C, F, X, num_cookies, prod_rate) 
    time_to_farm = (C/float(prod_rate))
    goal_cookies_time = X/float(prod_rate)            # time_till_goal_cookies(C, F, X, num_cookies, prod_rate)
    if next_farm_time >= goal_cookies_time:
      #time till the end
      total_time = total_time + goal_cookies_time
      done = True
    else:
      #Buy a farm
      prod_rate = prod_rate+F
      total_time = total_time + time_to_farm

  return total_time

def main():
  output = []
  with open(sys.argv[1]) as file:
    testcases = int(file.readline())
    
    for i in range(0, testcases):
      output.append(process_case(file.readline()))


  for i in range(0, len(output)):
    print "Case #"+str(i+1)+": " + str(output[i])
    

if __name__ == '__main__':
  main()
