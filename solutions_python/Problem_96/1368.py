import os,sys
import itertools

class google(object):
  def __init__(self, ng, ns, best, tot):
    self.ng = ng
    self.ns = ns
    self.best = best
    self.tot = tot
    self.n_good = 0
    all_p = itertools.permutations(range(self.ng))
    all_good=[]
    for p in all_p:
      n_good = 0
      self.this_ns = 0
      for ii in p:
        if( self.possible(self.tot[ii] ) ):
          n_good=n_good+1
      all_good.append(n_good)
    self.n_good = max(all_good)
    

  def print_out(self):
    print self.ng,self.ns,self.best,
    for t in self.tot:
      print t,
    print

  def possible(self, nt):
     mean = int(nt/3)
     possible_triplets, surprise = self.generate_triplets(mean,nt)
     if(surprise): self.this_ns = self.this_ns + 1
     for t in possible_triplets:
       if(max(t)>=self.best):
#         print max(t), self.best, self.n_good
         return True
     return False
     

  def generate_triplets(self,mean,nt):
     triplets = []
     if(self.ns == 0 ): r=1
     if(self.ns > 0 ): r=2
     this_ns = 0
     start = max(0,mean-r-1)
     end = min(10,mean+r+2)+1
     for ii in range(start,end):
       for jj in range(start,end):
         kk = nt -ii -jj
         if(kk<0 or kk>10): continue
         d12 = abs(kk-ii)
         d13 = abs(kk-jj)
         d23 = abs(ii-jj)
         if( d12<=r and d13<=r and d23<=r ):
           if( d12==2 or d13==2 or d23==2 ):
             this_ns = this_ns + 1
             if(self.this_ns >= self.ns): continue
             else: triplets.append( (ii,jj,kk) )
           else:
             triplets.append( (ii,jj,kk) )
             #print (ii,jj,kk)
     return triplets, (this_ns>0)
     

def readlines(filename):
  input=open(filename,'r')
  googlers=[]
  l = input.readline()
  nl=int(l )
  for ii in range(nl):
    this_line = input.readline().split('\n')[0]
    keys = this_line.split()
    ng=int(keys[0])
    ns=int(keys[1])
    best=int(keys[2])
    tot=[]
    for kk in range(ng):
      tot.append(int(keys[kk+3]))
    this_googler = google(ng,ns,best,tot)
    googlers.append( this_googler )
  return googlers


def run(args):
    filename = args[0]
    googlers = readlines( filename )
    ii=1
    for g in googlers:
      print "Case #%d: %d"%(ii, g.n_good)
      ii = ii + 1

#      print "Case #%d: %s"%(ii,str)
#      ii = ii + 1


if __name__ == "__main__":
  args=sys.argv[1:]
  run(args)
  
    
