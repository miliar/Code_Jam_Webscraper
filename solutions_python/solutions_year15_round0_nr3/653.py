import os,sys
leg = {
  '1':0,
  'i':1,
  'j':2,
  'k':3
  }

tab = [
  ['1','i','j','k'],
  ['i','-1','k','-j'],
  ['j','-k','-1','i'],
  ['k','j','-i','-1']]

def zap(x):
  return x[0]=='-'

def mi(x):
  if(zap(x)): return x[1:]
  else: return '-'+x

def krat(a,b):
  if zap(a): return mi(krat(mi(a),b))
  if zap(b): return mi(krat(a,mi(b)))
  return tab[leg[a]][leg[b]]  

vec = ""
def solve(T):
  a,b = map(int,raw_input().strip().split())
  print "Case #%d:"%T,
  vec = raw_input().strip()*b
  #print vec
  dasa = False
  q='1'
  i=0
  while q !='i' and i<len(vec)-2:
    q= krat(q,vec[i]);
    i+=1
  
  if i< len(vec) and q=='i':
    q='1'
    j=i
    while q !='j' and j<len(vec):
      q= krat(q,vec[j]);
      j+=1
    #print 'j', j
  
    if j< len(vec) and q=='j':
      q='1'
      k=j
      while k<len(vec):
        q= krat(q,vec[k]);
        k+=1
      #print k
      if q =='k':
        dasa=True;
  
  
  if dasa:
    print "YES"
  else:
    print "NO"

def main():
  
  #print krat(krat(krat('j','i'),krat('j','i')),krat('j','i'))
  #print krat('j',krat('i',krat('j',krat('i',krat('j','i')))))
  T=input()
  for x in xrange(T):
    solve(x+1)


main()