from collections import deque

input = open('A-large.in', 'r')
num_testcases = int(input.readline())

for testcase in range(1, num_testcases + 1):
  test_info = input.readline().split()
  #print "Test spec: ", test_info
  
  num_insns = int(test_info[0])
  test_info = zip(test_info[1::2], map(int, test_info[2::2]), range(1,num_insns + 1))
  
  #blue = deque()
  #orange = deque()
  
  blues = deque([(i, b) for (c, b, i) in test_info if c == 'B'])
  oranges = deque([(i, b) for (c, b, i) in test_info if c == 'O'])
  
  # (Instruction index, Button number)
  #print "Blues:", blues
  #print "Oranges:", oranges
  
  # Now that we've parsed our input into a usable format,
  # let's solve it! :)
  b = 1 # Blue's current position
  o = 1 # Orange's current position
  i = 1 # The current instruction's index
  t = 0 # The current timestep
  
  #print "Time | Orange             | Blue"
  #print "-----+--------------------+-------------------"
  
  while i <= num_insns:
    t = t + 1
    #print str(t).center(5) + "| ",
    next_insn = False
    
    # Is orange done?
    if len(oranges) > 0:
      # Is orange at the right location?
      (insn_ix, insn_button) = oranges[0]
      if o < insn_button:
        o = o + 1
        #print "Move to button", o,
      elif o > insn_button:
        o = o - 1
        #print "Move to button", o,
      elif o == insn_button and insn_ix == i:
        #print "Push button", o,
        oranges.popleft()
        next_insn = True
    
    # Is blue done?
    if len(blues) > 0:
      # Is blue at the right location?
      (insn_ix, insn_button) = blues[0]
      if b < insn_button:
        b = b + 1
        #print "Move to button", b,
      elif b > insn_button:
        b = b - 1
        #print "Move to button", b,
      elif b == insn_button and insn_ix == i:
        #print "Push button", b,
        blues.popleft()
        next_insn = True
    
    #print "" # New line :)
    
    if next_insn:
      i = i + 1
  # end for
  print "Case #" + str(testcase) + ":", t