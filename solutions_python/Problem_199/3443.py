t = int(raw_input())

for i in xrange(1, t + 1): 
  s, k = raw_input().split(" ")
  s = list(s)
  k = int(k)

  min_num_flips = 0
    
  for x in range(len(s)-(k-1)):
    if s[x] == '-':
      for y in range(k):
        s[x+y] = '+' if s[x+y] == '-' else '-'
      min_num_flips += 1
        
  for z in range(len(s)-(k-1), len(s)):
    if s[z] == '-':
      min_num_flips = 'IMPOSSIBLE'
                
  print "Case #{}: {}".format(i, min_num_flips)
