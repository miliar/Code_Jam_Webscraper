def ops(x):
 if x=='X':
  return 'O'
 return 'X'

def check_go(i,j,x,y,field,type):
 try:
  nubT=0
  #print i,j,x,y,type
  for _ in range(4):
   if x<0 or y<0 or x>=4 or y>=4:
    return 0
   now = field[x][y]
   #print now,
   if now==ops(type) or now=='.':
    return 0
   
   if now=='T':
    nubT+=1
   x+=i
   y+=j
  if nubT<=1:
   return 1
 except:
  return 0

def check(field):
 nub_point=0
 for x in range(4):
  for y in range(4):
    if field[x][y]=='.':
     nub_point+=1	
    for i in range(-1,2):
     for j in range(-1,2):
      if i==0 and j==0:
	   continue;
      X=check_go(i,j,x,y,field,'X')
      #print
      O=check_go(i,j,x,y,field,'O')
      #print
      if X :
       return "X won"
      if O :
	   return "O won"
	   
    
 if nub_point:
  return "Game has not completed"
 return "Draw"
 
 
 
n = input()

for _ in range(n):
 s = []
 for __ in range(4):
  s.append(raw_input()) 
 if n-1-_ : raw_input()
 print "Case #"+str(_+1)+": "+check(s)
