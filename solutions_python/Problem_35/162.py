
newsinkid=1

def find_sink(x,y,W,H,cells,sinks):
   global newsinkid
   if sinks[y][x]!=0:
      return sinks[y][x]
   dirs=(0,-1), (-1,0), (1,0), (0,1)
   h=cells[y][x]
   low=999999
   lowpos=(0,0)
   for d in dirs:
      xx,yy=x+d[0], y+d[1]
      if (xx<0 or yy<0 or xx>=W or yy>=H):
         continue
      hh = cells[yy][xx]
      if hh<low:
         low=hh
         lowpos=(xx,yy)
   if low<h:
      s=find_sink(lowpos[0], lowpos[1],W,H,cells,sinks)
      sinks[y][x]=s
      return s
   else:
      # im a sink
      id=newsinkid
      sinks[y][x]=id
      newsinkid+=1
      return id

f=open('B-large.in')
#f=open("B-small-attempt0.in")
#f = open('2.test')
T = int(f.readline())
casenum=1
for n in range(0, T):
   newsinkid=1
   line=f.readline().strip().split()
   H=int(line[0])
   W=int(line[1])
   cells=[]
   sinks=[]
   for row in range(0, H):
      r=[int(x) for x in f.readline().strip().split()]
      sinks.append([0]*len(r))
      cells.append(r)
   sinklist={}
   s=0
   for y in range(0, H):
      for x in range(0, W):
         oid=newsinkid
         if oid==find_sink(x,y,W,H,cells,sinks):
            sinklist[oid]=chr(ord('a')+s)
            s+=1
   print("Case #"+str(casenum)+":")
   casenum+=1
   for y in range(0, H):
      sinkline=""
      for x in range(0, W):
         sinkline+=sinklist[sinks[y][x]]+" "
      print(sinkline.strip()) 
         

