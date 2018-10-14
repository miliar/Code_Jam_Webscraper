test_cases = int(raw_input())
for test_case in xrange(1,test_cases+1):
   problem = raw_input().split(' ')

   def str_to_tla(str):
      if len(str) == 2:
         return (str[0], str[1])
      elif len(str) == 3:
         return (str[0], str[1], str[2])
      else:
         print len(str)
         print 'AAAUUUGGGHHH'
         exit()

   combine_count = int(problem[0])
   if combine_count > 0:
      combine = problem[1:(combine_count + 1)]
      combine = [ str_to_tla(x) for x in combine ]
   else:
      combine = []

   opposed_count = int(problem[combine_count + 1])
   if (opposed_count > 0):
      opposed = problem[(combine_count + 2):(combine_count + opposed_count + 2)]
      opposed = [ str_to_tla(x) for x in opposed ]
   else:
      opposed = []

   invoke_count = int(problem[combine_count + opposed_count + 2])
   invoke_seq = problem[combine_count + opposed_count + 3]
   invoked = []

   for element in invoke_seq:
      if len(invoked) > 0:
         recent = invoked[-1]
         combined = 0
         for x in combine:
            if (x[0] == element and x[1] == recent) or (x[1] == element and x[0] == recent):
               combined = 1
               invoked[-1] = x[2]
         if combined == 0:
            invoked.append(element)
         for i in xrange(len(invoked)):
            for j in xrange(len(invoked)):
               for opp in opposed:
                  if (i != j and len(invoked)):
                     if (invoked[i] == opp[0] and invoked[j] == opp[1]) or \
                        (invoked[i] == opp[1] and invoked[j] == opp[0]):
                        invoked = []
      else:
         invoked.append(element)
         
   output = '[' + ', '.join(invoked) + ']'
   print "Case #" + str(test_case) + ":", output
