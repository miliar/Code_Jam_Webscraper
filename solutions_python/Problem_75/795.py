import string

# This is one of the dirtiest codes I have ever written O_o

f = open('B-large.in')
o = open('out', 'w')
cases = int(f.readline())

for case in range(0, cases):
  l = f.readline()
  chunks = string.split(l)
  
  combinations = int(chunks[0])
  combs = {}
  
  for i in range (0, combinations):
    comstr = chunks[1+i]
    if (not comstr[0] in combs):
      combs[comstr[0]] = []  
    combs[comstr[0]].append([comstr[1], comstr[2]])
    if (not comstr[1] in combs):
      combs[comstr[1]] = []  
    combs[comstr[1]].append([comstr[0], comstr[2]])    
   
  opponents = int(chunks[1 + combinations])
  ops = {}
  
  for i in range (0, opponents):
    opstr = chunks[2 + combinations + i]
    if (not opstr[0] in ops):
      ops[opstr[0]] = []
    ops[opstr[0]].append(opstr[1])
    if (not opstr[1] in ops):
      ops[opstr[1]] = []    
    ops[opstr[1]].append(opstr[0])
  
  print combs
  print ops
  
  buildorder = chunks[combinations + opponents + 3]
  
  stack = []
  
  for char in buildorder:
    # Check if element can be combined
    append = True
    if char in combs:
      try:
        last = stack[len(stack)-1]
        for com in combs[char]:
          if com[0] == last:
            append = False
            stack.pop()
            stack.append(com[1])
      except Exception:
        print "E"
    
    # Check if Opposing elements are there
    if append and (char in ops):
      for op in ops[char]:
        if op in stack:
          stack = []
          append = False
    
    if append:  
      # Just append it
      stack.append(char)   
  
  print 'Case #' + str(case+1) + ': [' + ', '.join(stack) + ']'
  o.write('Case #' + str(case+1) + ': [' + ', '.join(stack) + ']\n')
  
o.close()
f.close()
  


