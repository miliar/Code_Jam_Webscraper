filename = 'B-small-attempt3'
input  = open(filename+'.in')
output = open(filename+'.out','w')

T = int(input.readline().strip())

for t in range(T):
  R,C = [int(x) for x in input.readline().strip().split(' ')]
  map = [[[int(x),False] for x in 
           input.readline().strip().split(' ')]
         for r in range(R)]
  output.write('Case #%s:\n'%(t+1,))

  def nextbasin():
    nextbasin.basin = chr(ord(nextbasin.basin)+1)
    return nextbasin.basin
  nextbasin.basin = chr(ord('a')-1)

  neighbors = [(-1,0),(0,-1),(0,1),(1,0)]
  def bestneighbor(map,r,c):
    br,bc,a = -1,-1,map[r][c][0]
    for relneighbor in neighbors:
      neighbor = r+relneighbor[0],c+relneighbor[1]
      if( 0<=neighbor[0]<len(map) and 
          0<=neighbor[1]<len(map[neighbor[0]])):
        b = map[neighbor[0]][neighbor[1]][0]
        if b<a:
          a = b
          br,bc = neighbor
    return br,bc       
  
  replace = {}
  maxch = chr(ord('a')+R*C)
  for ordch in range(ord('a'),ord(maxch)):
    replace[chr(ordch)] = 0
    
  for r in range(R):
    for c in range(C):
      nr,nc = bestneighbor(map,r,c) #returns -1,-1 if not found
      if not map[r][c][1]:
        map[r][c][1] = nextbasin()
      ch = map[r][c][1]
      if ch not in replace:
        replace[ch] = 0
      if nr>=0 and nc>=0:
        nch = map[nr][nc][1]
#        print(r,c,ch,nr,nc,nch)
        if nch and nch!=ch:       
#          if ch<nch:
#            ch,nch = nch,ch
          replace[ch] = (nch if isinstance(nch,int) or
                                isinstance(replace[ch],int) else
                          min(nch,replace[ch]))
          for ordch in range(ord(ch)+1,ord(maxch)):
            if isinstance(replace[chr(ordch)],int):
              replace[chr(ordch)] -= 1
        else:
          map[nr][nc][1] = map[r][c][1]

#  for r in range(R):
#    print(' '.join([map[r][c][1] for c in range(C)]))

  for r,v in replace.copy().items():
    if v==0:
      del replace[r]
    
#  print(replace)


  for r in range(R):
    for c in range(C):
      lastch = map[r][c][1]
      ch = map[r][c][1]
      while True:
        if isinstance(ch,int):
          map[r][c][1] = chr(ord(lastch)+ch)
          break
        else:
          if ch not in replace:
            map[r][c][1] = ch
            break
          else:
            lastch = ch
            ch = replace[ch]           
                        
  
  for r in range(R):  
    output.write(' '.join([map[r][c][1] for c in range(C)])+'\n')

