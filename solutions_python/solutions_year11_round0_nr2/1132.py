
combinations = {}
oposed = {}

def calculate(sequence):
  stack = []
  sequence.reverse()
  while(len(sequence)>0):
    stack.append(sequence.pop())
    if(len(stack)<2):
      continue
    target = stack[-2]+stack[-1]
    if target in combinations:
      stack.pop()
      stack.pop()
      stack.append(combinations[target])
    elif stack[-1] in oposed:
      if oposed[stack[-1]] in stack:
        stack = []
      #target=stack[-1]
      #if oposed[target] in stack:
      #  while(stack.pop()!=oposed[target]):
      #    continue
  return stack
      

n_tests = int(raw_input())
for test in xrange(n_tests):
  combinations = {}
  oposed = {}
  sequence = []
  
  start = True
  comb = True
  opo = True
  
  line = raw_input().split()
  for element in line:
    if(start):
      start = False
    elif(comb):
      if(element>='0' and element <='99999'):
        comb = False
      else:
        combinations[element[0]+element[1]]=element[2]
        combinations[element[1]+element[0]]=element[2]
    elif(opo):
      if(element>='0' and element <='99999'):
        opo = False
      else:
        oposed[element[0]]=element[1]
        oposed[element[1]]=element[0]
    else:
      for c in element:
        sequence.append(c)

  
  result = calculate(sequence)
  final = ""
  first = True
  for element in result:
    if(first):
      final = final + element
      first = False
    else:
      final = final +", "+element
  
  print "Case #%d: [%s]" %(test+1,final)