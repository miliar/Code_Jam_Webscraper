import bisect

def reverse_insort(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it reverse-sorted assuming a
    is reverse-sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid+1
    a.insert(lo, x)

iFile = open("A-small-attempt2.in","r")
oFile = open("output.txt","w")

cases = int(iFile.readline().strip())

for i in range(cases):

  routes = []
  loss = 0

  line = iFile.readline()
  N = int(line.split()[0])
  M = int(line.split()[1])
  
  for j in range(M):
    
    line = iFile.readline()
    routes.append([int(line.split()[0]),int(line.split()[1]),int(line.split()[2])])
  
  origins = routes[:]
  origins.sort(reverse=True)
  ends = routes[:]
  ends.sort(key=lambda x:x[1])
  
  swapped = True
  while swapped:
    swapped = False
    for group in ends:
      for available in origins:
        if group[2] == 0:
            break
        if available[0] <= group[1]:
          possible = min(available[2],group[2])
          if possible != 0:
            loss += possible*(available[0]-group[0])*(available[1]-group[1])
            loss = loss % 1000002013
            group[2] = group[2] - possible
            if group != available:
              available[2] = available[2] - possible
              swapped_group = [group[0],available[1],possible]
              routes.append(swapped_group)
              origins = routes[:]
              origins.sort(reverse=True)
              ends = routes[:]
              ends.sort(key=lambda x:x[1])
              swapped = True
          if swapped == True: break
        if swapped == True: break
        
          
  
  
  output = str(loss)

  oFile.write("Case #"+str(i+1)+": "+output+"\n")
