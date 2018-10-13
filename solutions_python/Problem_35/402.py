#!/usr/bin/python
# hfgr 2009, alien problem of codejam 2009


def where(x,y):
   N=False
   Nv=9999
   S=False
   Sv=9999
   E=False
   Ev=9999
   W=False
   Wv=9999
   act=int(mat[x][y])
   if (x+1)<Hh and int(mat[x+1][y])<act:
   #   print 'S'
      Sv = int(mat[x+1][y])
      S=True
   #   print 'S true'
   if (y+1)<Ww and int(mat[x][y+1])<act:
   #   print 'E'
      Ev=int(mat[x][y+1])
      if S and Ev<=Sv:
        E=True
        S=False
   #     print 'E true'
      elif not S: 
         E=True
   #      print 'E true'
   if (y-1)>=0 and int(mat[x][y-1])<act:
   #   print 'W'
      Wv=int(mat[x][y-1])
      if E and Wv<=Ev:
        W= True
        E= False
   #     print 'W true'
      elif S and Wv<=Sv:
        W=True
        S=False
   #     print 'W true'
      elif not(E or S):
        W=True
   #     print 'W true'
  
   if (x-1)>=0 and int(mat[x-1][y])<act:
   #   print 'N'
      Nv=int(mat[x-1][y])
      if W and Nv <= Wv:
         N=True
	 W=False
   #      print 'N true'
      elif E and Nv <= Ev:
         N=True
         E=False
   #      print 'N true'
      elif S and Nv <= Sv:
         N=True
         S=False      
   #      print 'N true'
      elif not(W or E or S):
         N=True
   #      print 'N true'
   
   if N:
      return [x-1,y]
   elif W:
      return [x,y-1]
   elif E:
      return [x,y+1]
   elif S:
      return [x+1,y]
   else: 
      return [x,y]



def busca(x,y):
        global last
        res1=where(x,y)
        nx=res1[0]
        ny=res1[1]
        #find a sink
        if nx==x and ny==y:
           if mate[x][y] == '*':
              mate[x][y]=cadena[last]
              last+=1
           return mate[x][y]
        else:
           mate[x][y] = busca(nx,ny)
           return mate[x][y]


last=0
cadena="abcdefghijklmnopqrstuvwxyz"
F = open('input-corto.txt')
casos= int(F.readline()[:-1])
for c in range(1,casos+1):
  print "Case #"+str(c)+":"
  last=0
  linea = F.readline()[:-1].split()
  Hh = int(linea[0])
  Ww = int(linea[1])
  mate =[]
  mat=[]
  for x in range(Hh):
    mat.append(F.readline()[:-1].split())
    mate.append( ("* "*Ww).split()) # mark the labeled matrix
  # After the lecture, calculate the fall
  for xx in range(Hh):
    for yy in range(Ww):
      if mate[xx][yy]=='*':
         mate[xx][yy]=busca(xx,yy)
  # print the results
  for r in mate:
    print ' '.join(r)
 
             
      
