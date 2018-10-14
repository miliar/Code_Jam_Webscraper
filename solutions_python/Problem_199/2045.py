"""

"""

class OversizedPancakeFlipper(object):
  """
  """
  
  def countFips(self, test):
    """ """
    flips, conseq, maxSame = 0, 1, 1
    refVal = test[0]
    if test[0] == '-':
      flips += 1
    for i in range(1, len(test)):
      if refVal != test[i]:
        print 'test'
        flips += 1
        maxSame = max(maxSame, conseq)
        conseq = 1
        refVal = test[i]
      else:
        conseq += 1
    return flips, maxSame
  
  def flip(self, data, k):
    """
    """
    for i, val in enumerate(data[:-k+1]):
      if val == False:
        j = 0
        while True:
          data[i+j] = not data[i+j]
          j += 1
          if j >= k:
            break
          
        return data

    return data
    
  def execute(self, inFile, outFile):
    """
    """
    numberTest = int(inFile.next())
    print "Running %s tests" % numberTest
    for i, line in enumerate(inFile):
      test, k = line.strip().split(' ')
      stack = [False if val == '-' else True for val in test]
      size = len(test)
      res = all(item for item in stack)
      if res:
        outFile.write("Case #%s: 0\n" % (i+1))
        continue
      
      for t in range(size):
        stack = self.flip(stack, int(k))
        res = all(item for item in stack)
        if res:
          t += 1
          break
        
      else:
        outFile.write("Case #%s: IMPOSSIBLE\n" % (i+1))
        continue
      
      outFile.write("Case #%s: %s\n" % (i+1, t))
#       attempt = int(k)
#       flips, maxSame = self.countFips(test)
#       if sum(stack) == size:
#         outFile.write("Case #%s: 0\n" % (i+1))
#       else:
#         if maxSame < int(k):
#           outFile.write("Case #%s: IMPOSSIBLE\n" % (i+1))
#         else:
#           outFile.write("Case #%s: %s\n" % (i+1, flips-1))
#       print stack 
#       
#       flips, maxSame = self.countFips(test)
#       if flips == 0:
#         if test.startswith('-'):
#           mod = size % int(k)
#           if mod == 0:
#             outFile.write("Case #%s: %s\n" % (i+1, size / int(k)))
#           else:
#             outFile.write("Case #%s: IMPOSSIBLE\n" % (i+1))
#         else:
#           outFile.write("Case #%s: 0\n" % (i+1))
#       else:
#         if maxSame < int(k):
#           outFile.write("Case #%s: IMPOSSIBLE\n" % (i+1))
#         else:
#           outFile.write("Case #%s: %s\n" % (i+1, flips-1))
