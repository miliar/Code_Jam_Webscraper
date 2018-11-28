numCases = int(raw_input())
combine = {}
oppose  = {}

for i in xrange(numCases):
   line = raw_input().split()
   line.reverse()
   combine = {}
   numComs = int(line.pop())
   
   # reading the combinations into a hash table
   for j in xrange(numComs):
      com = line.pop()
      combine[com[:2]] = com[2]
   
   oppose = {}
   numOpposed = int(line.pop())
   
   for j in xrange(numOpposed):
      opp = line.pop()
      if opp[0] in oppose:
         oppose[opp[0]].append(opp[1])
      else:
         oppose[opp[0]] = [opp[1]]
      if opp[1] in oppose:
         oppose[opp[1]].append(opp[0])
      else:
         oppose[opp[1]] = [opp[0]]
      
   size = line.pop()
   invoke = list(line.pop())
   invoke.reverse()
   stack = []
   element = ' '
   while len(invoke) != 0:
      stack.append(invoke.pop())
      if len(stack) != 1:
         element = stack.pop()
         top     = stack.pop()
         used = False
         if element + top in combine:
            stack.append(combine[element+top])
            used = True
         elif top + element in combine:
            stack.append(combine[top+element])
            used = True
         else:
            stack.append(top)
            stack.append(element)
         if element in oppose and not used:
            for bomb in oppose[element]:
               if bomb in stack:
                  #print stack
                  stack = []
                  #print element, bomb, 'found, list exploded'
         #print stack
            # print element, 'appended'
   print 'Case #' + str(i+1) + ': [' + ', '.join(stack) + ']'
