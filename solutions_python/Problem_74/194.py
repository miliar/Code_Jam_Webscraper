from repr import repr


    
input  = open('../input/Q_2011_a.in')
CASES  = int(input.readline())


for case in range(CASES):
  sequence = input.readline().rstrip().split(' ')[1:]
  size= len(sequence)
  steps=[]
  for i in range(0,size,2):
    steps.append((sequence[i],int(sequence[i+1])))
  
  posB=1
  posO=1
  timeB=0
  timeO=0
  timeSpent=0
  for st in steps:
    if st[0]=='O':
      goTo = st[1]
      timeO+=abs(posO-goTo)+1
      if timeO<=timeSpent:
        timeSpent+=1
        timeO=timeSpent
      else:
        timeSpent=timeO
      posO=goTo
    elif st[0]=='B':
      goTo = st[1]
      timeB+=abs(posB-goTo)+1
      if timeB<=timeSpent:
        timeSpent+=1
        timeB=timeSpent
      else:
        timeSpent=timeB 
      posB=goTo
  
    
  print 'Case #'+str(case+1)+': '+str(timeSpent)
  