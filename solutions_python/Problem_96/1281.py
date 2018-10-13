
T = int(raw_input())
for i in range(T):
    mx = 0
    l = (raw_input()).split()
    n, s, p = int(l[0]), int(l[1]), int(l[2])
    for j in range(3, len(l)):
      if int(l[j]) >= (3*p-2):
        mx = mx + 1
      elif int(l[j]) < (3*p-4):
        mx =  mx + 0
      elif (3*p-4>0):
        if s > 0:
          mx = mx + 1
          s = s - 1
    print "Case #%d: %d" %(i+1, mx) 
    
