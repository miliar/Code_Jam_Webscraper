
def readmat_row(f,total,row):
   for r in range(total):
      rr = f.readline()
      if r == row-1:
         retval = rr
   return retval

f = open('in')
cases = int(f.readline())

for case in range(cases):

   r1 = int(f.readline())
   data1 = readmat_row(f,4,r1).split()
   my1 = dict( (t,t) for t in data1 )

   r2 = int(f.readline())
   data2 = readmat_row(f,4,r2).split()
   out = []
   for i in data2:
      if i in my1:
         out.append(i)
   if len(out) == 1:
      print "Case #%d: %s"%(case+1, out[0])
   elif len(out) == 0:
      print "Case #%d: Volunteer cheated!"%(case+1)
   else:
      print "Case #%d: Bad magician!"%(case+1)

