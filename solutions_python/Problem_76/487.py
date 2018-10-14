from operator import xor

input = open('C-large.in', 'r')
num_testcases = int(input.readline())

for testcase in range(1, num_testcases + 1):
  num_candies = int(input.readline())
  #print num_candies, "candies"
  
  candy_info = map(int, input.readline().split())
  #print "Candy info: ", candy_info
  
  print "Case #" + str(testcase) + ":",
  if reduce(xor, candy_info) <> 0:
    print "NO"
  else:
    print sum(candy_info) - min(candy_info)