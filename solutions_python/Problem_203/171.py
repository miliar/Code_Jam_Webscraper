fin = open("A-large.in","rt")

t = fin.readline().rstrip('\n')
t = int(t)

fout = open("OUTPUT","wt") 

for ex in range(t):
     r = fin.readline().rstrip('\n').split(' ')
     c = int(r[1])
     r = int(r[0])
     cake = []
     for row in range(r):
         cake.append(list(fin.readline().rstrip('\n')))
     print
     for h in cake:
         print "".join(h)
     for x in range(r):
         y = 0
         stopper = 0
         while y<c:
             if cake[x][y] != '?':
                 ini = cake[x][y]
                 y += 1
                 while y<c and cake[x][y] == '?':
                     y+=1
                 y -= 1
                 ii = 1
                 for z in range(stopper,y+1):
                     cake[x][z] = ini
                 while x-ii >= 0 and cake[x-ii][y] == '?':
                     for z in range(stopper,y+1):
                         cake[x-ii][z] = ini
                     ii += 1
                 stopper = y+1
             y += 1
     nucake = []
     sig = []
     for x in cake:
         if '?' in x:
             nucake.append(sig)
             continue
         nucake.append(x)
         sig = x
     s = "Case #"+str(ex+1)+":\n"
     lss = []
     for j in nucake:
         lss.append("".join(j))
     s += "\n".join(lss)
     s += "\n"
     fout.write(s)
     print s,
        
   
fout.close()
