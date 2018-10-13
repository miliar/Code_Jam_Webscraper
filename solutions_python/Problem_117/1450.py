import os
fname = 'B-small-attempt1'

f = open(fname+'.in')
lines = f.readlines()
f.close()

numcases = int(lines[0])
def canCut(desiredlawn):
    for r in range(rows):
        for c in range(cols):
             col = [X[c] for X in desiredlawn]
             row = desiredlawn[r]
             value = desiredlawn[r][c]
             rowg  =sum(i > value  for i in row)
             colg = sum(i > value  for i in col)
             if( rowg > 0 and colg > 0):
                 return False
    return True

         

lines.pop(0)

f = open(fname+'.out','w')

for i in range(1,numcases+1):
       listline = lines[0].strip().split(' ')
       rows = int(listline[0])
       cols = int(listline[1])
       lines.pop(0)
       lawn = [[100 for x in xrange(cols)] for x in xrange(rows)]
       desiredlawn = [[0 for x in xrange(cols)] for x in xrange(rows)]
       for r in range(rows):
           desiredlawn[r] = lines[0].strip().split(' ')
           lines.pop(0)

       if(canCut(desiredlawn)):
         f.write("Case #{0}: YES\n".format(i))
       else:
         f.write("Case #{0}: NO\n".format(i))
         

             
         
           
       

           
       print desiredlawn

    

f.close()  
