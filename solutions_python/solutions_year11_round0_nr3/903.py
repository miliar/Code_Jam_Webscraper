import sys

#isprint = True
isprint = False 
def comment(t):
  if(isprint): print t

def calc(a,p):
  if len(a) == len(p): return False
  x1 = 0
  x2 = 0
  for i in xrange(len(a)):
    if i in p: x1 = x1^a[i]
    else: x2 = x2^a[i] 
  return x1 == x2 
     
if __name__ == '__main__':
  data = open(sys.argv[1])
  n_case = int(data.readline().strip())
  for n in xrange(1,n_case+1):
    n_candy = int(data.readline().strip())
    candy_array = [int(x) for x in data.readline().strip().split() ] 
    comment(candy_array)
    sum_ca = sum(candy_array)
    l = len(candy_array)
    queue = []
    max_pile = -1
    for i in xrange(l):
      queue.append([i])
    while queue != []:
      q = queue.pop()
      if calc(candy_array,q):
        s1 = sum([candy_array[j] for j in q]) 
        s2 = sum_ca - s1
        if max(s1,s2) > max_pile: max_pile = max(s1,s2)       
      
      last_p = q[len(q)-1]
      if last_p != l-1 :
        for j in xrange(last_p + 1,l):
          x = q[:]
          x.append(j)
          queue.append(x)

      comment('queue : ' + repr(queue))
      comment('max_pile : ' + str(max_pile))
      #raw_input()
 
    if max_pile == -1 : print "Case #%d: NO"%n
    else: print "Case #%d: %d"%(n,max_pile)
    
