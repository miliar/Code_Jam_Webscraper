#!/usr/bin/python

# Snappers
# jk

# initialize
test_case_num = 0
max_test_case = int(raw_input())

#twos = [ 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768,
#65536, 131072, ]

# loop on test cases
for test_no in range(max_test_case):

  test_case_num += 1
  #print "Test case #%d" % test_case_num

  # first line of test case config
  line = raw_input()
  line_elems = line.split(' ')

  # N k
  snapper_num = int(line_elems[0])
  snapping_num = int(line_elems[1])
  
  #print "N=%d, k=%d" % (snapper_num, snapping_num)

  # process a test
  
  # init
  bState = False
  bStarted = False
  
  # dissect snapping num to binary
  
  # find largest num yet smaller than the snapping num
  max_two = 1
  count = 0
  str = ""

  if 0 == snapping_num:
    max_two = 1 # error out

  while max_two <= snapping_num:
    max_two *= 2
    count += 1

  #print ": 2^%d" % count
  
  # constructing binary
  while max_two >= 1:
    if snapping_num >= max_two:
      if not bStarted:
        bStarted = True
        
      snapping_num -= max_two
      str += "1"
    elif bStarted:
      str += "0"

    max_two /= 2
  
  #print "str: %s" % str
  #print "digits: %d" % len(str)
  
  # check sraight ones
  count = 0
  for i in str[::-1][:snapper_num]:
    if "1" == i:
      count += 1
  
  if count == snapper_num:
    bState = True
 
  if bState == True:
    print "Case #%d: ON" % (test_no+1)
  else:
    print "Case #%d: OFF" % (test_no+1)