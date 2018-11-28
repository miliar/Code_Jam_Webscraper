#!/usr/bin/python

# Theme park
# jk

# initialize
test_case_num = 0
max_test_case = int(raw_input())

# loop on test cases
for test_no in range(max_test_case):

  test_case_num += 1
  # print "Test case #%d" % test_case_num

  # first line of test case config
  line = raw_input()
  line_elems = line.split(' ')
  
  # R k n
  max_ride_count = int(line_elems[0])
  max_ppl_count = int(line_elems[1])
  max_group_count = int(line_elems[2])
  
  # print "R=%d, k=%d, N=%d" % (max_ride_count, max_ppl_count, max_group_count)

  # second line of test case config
  group_line = raw_input()
  group_str = group_line.split(' ')
  
  groups = []
  for i in range(len(group_str)):
    groups.append(int(group_str[i]))

  # if len(groups) != max_group_count:
  #  print "Input is wrong!"

  # process the round
  
  total_earn = 0
  
  # loop on each ride
  for i in range(max_ride_count):
    
    #print "Ride #%d" % (i+1)
    
    # init
    fill = 0
    riders = []
    
    # while the ride isn't full
    while True:
      # print "Fill=%d" % fill
      # print groups
      space = max_ppl_count - fill;
      if len(groups)!=0 and space >= groups[0]:
        fill += groups[0]
        cur = groups.pop(0)
        riders.append(cur)
      else:
        total_earn += fill
        break

    # restore the riders to back of the line
    groups += riders
    
  print "Case #%d: %d" % (test_no+1, total_earn)