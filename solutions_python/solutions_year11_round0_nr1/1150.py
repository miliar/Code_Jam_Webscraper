n_tests = int(raw_input())
for test in xrange(n_tests):
  unformated_sequence = raw_input().split()
#  print unformated_sequence

  sequence = []
  blue = []
  orange = []
  b = 1
  o = 1
  timer = 0
  first = True
  type_ = None
  for element in unformated_sequence:
    if(first):
        first = False
        continue
    if(type_==None):
      type_ = element
    else:
      t = (type_, int(element))
      type_=None
      sequence.append(t)
      if(t[0]=='O'):
        orange.append(t)
      else:
        blue.append(t)
        
#  print sequence
#  print blue
#  print orange
#  print
  

  timer = 0
  while(len(sequence)>0):
    #print timer, sequence, b,o
    poped = False
    if(len(blue)>0):
      if(b<blue[0][1]):
        b = b + 1
      elif(b>blue[0][1]):
        b = b - 1
      elif(blue[0]==sequence[0]):
        poped = True
        blue.pop(0)
        sequence.pop(0)
      
    if(len(orange)>0):
      if(o<orange[0][1]):
        o = o + 1
      elif(o>orange[0][1]):
        o = o-1
      elif(orange[0]==sequence[0] and not poped):
        orange.pop(0)
        sequence.pop(0)  
    
    timer +=1    
  print "Case #%d: %d" % (test+1,timer)
        
        

    
  