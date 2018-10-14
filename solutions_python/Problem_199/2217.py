def findOdds(s):
  index = s.find('-')
  return index

def flip(s):
  s= s.replace('-', '=')
  s= s.replace('+', '-')
  s= s.replace('=', '+')
  return s
  
def checkFinal(s):
  if '-' in s:
    return False
  else:
    return True
  
#print flip("+++")
#print findOdds("++-+")
tests = input("")
#print tests
for test in range(tests):
  table= {}
  score= {}
  pancake, size = [s for s in raw_input().split(" ")]
  flipsize = int(size)
  #print len(pancake)
  #print flipsize
  count = 0
  i=0 

  while (i+flipsize) <= len(pancake):
      index = findOdds(pancake)
      if((index+flipsize)> len(pancake)):
        break
      #print "index:", index
      if(index > -1):
        flipped = flip(pancake[index:index+flipsize])
        pancake = pancake[0:index]+flipped + pancake[index+flipsize:]
        #print "new pancake", pancake
        count = count + 1
        i = index+1
      else:
        i = i+flipsize

  #print "i", i
  if i>=len(pancake) or checkFinal(pancake[i:]):
    print "Case #" + str(test+1) +": "+ str(count)
  else:
    print "Case #" + str(test+1) +": IMPOSSIBLE" 
    
    
    
