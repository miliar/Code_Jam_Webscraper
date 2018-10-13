def rec_stall(n):
  res = []
  if n == 1: return stalls[1]
  if n == 2: return stalls[2]
  if n == 3: return stalls[3]
  if n%2 == 0:
    a = rec_stall(n/2)
    b = rec_stall(n/2-1)
    res.extend([[n/2-1,n/2]])
    c = [list(x) for x in zip(a,b)]
    c = [val for sublist in c for val in sublist]
    res.extend(c)
    res.extend([[0,0]])
    return res
  else:
    a = rec_stall(n/2)
    res.extend([[n/2,n/2]])
    c = [list(x) for x in zip(a,a)]
    c = [val for sublist in c for val in sublist]
    res.extend(c)
    res.extend([[0,0]])
    return res

stalls = [0,0,0,0]
stalls[1] = [[0,0]]
stalls[2] = [[0,1],[0,0]]
stalls[3] = [[1,1],[0,0],[0,0]]
#stalls[4] = [[1,2],[0,1],[0,0],[0,0]]
#stalls[5] = [[2,2],[0,1],[0,1],[0,0],[0,0]]
#stalls[6] = [[2,3],[1,1],[0,1],[0,0],[0,0],[0,0]]

#print 1,rec_stall(1)
#print 2,rec_stall(2)
#print 3,rec_stall(3)
#print 4,rec_stall(4)
#print 5,rec_stall(5)
#print 6,rec_stall(6)
#print 7,rec_stall(7)
#print 8,rec_stall(8)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  if n == m:
    print "Case #{}: {} {}".format(i, 0, 0)
    continue
  s = rec_stall(n)
  #print "Case #{}: {} {}", i, s, n, m, max(s[m-1]), min(s[m-1])
  print "Case #{}: {} {}".format(i, max(s[m-1]), min(s[m-1]))
