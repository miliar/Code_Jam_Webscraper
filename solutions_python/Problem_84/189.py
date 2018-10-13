red = []
red.append(['/','\\'])
red.append(['\\','/'])


ntests = int(raw_input())
for test in xrange(ntests):
  size = map(int,raw_input().split())
  piece = []
  for i in xrange(size[0]):
    piece.append(list(raw_input()))
    
  
  y=0
  x=0
  valid = True
  while(y<size[0]):
    x=0
    while(x<size[1]):
#      print x,y,piece[y][x]
      if(piece[y][x]=='#'):
        if(x==size[1]-1 or y==size[0]-1):
          valid=False
          break

        piece[y][x]='/'
        if(piece[y][x+1]=='#'):
          piece[y][x+1]='\\'
        else:
          valid = False
        if(piece[y+1][x]=='#'):
          piece[y+1][x]='\\'
        else:
          valid=False
        if(piece[y+1][x+1]=='#'):
          piece[y+1][x+1]='/'
        else:
          valid=False            
      x+=1
    y+=1
    
#  print valid
#  for i in xrange(size[0]):
#    print piece[i]

  print "Case #%d:" % (test+1)
  if valid:
    for i in xrange(size[0]):
      print "".join(piece[i])
  else:
    print "Impossible"
    
    
