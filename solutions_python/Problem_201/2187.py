import math

def solve(N, K):
    if K == 1:
      return N/2, (N-1)/2
    else:
      # print N
      n = int(math.floor(math.log(K,2)))
      if N % 2 == 0:
        S = {N/2:1, (N-1)/2:1} # Stores the dictionary of count of that space
      else:
        S = {(N-1)/2:2, (N/2 - 1):0}
      curr = N/2
      for i in range(n):
        a = curr / 2
        b = a-1
        # print "a,b,curr:",a,b,curr
        # Get the count of a and b and add to dictionary
        if (curr % 2 == 0):
          # if curr is even then a gets curr's count
          S[a] = S[curr]
          S[b] = S[curr] + S[curr - 1]*2
        else:
          # print curr
          # print S/
          S[a] = S[curr]*2 + S[curr - 1]*1
          S[b] = S[curr-1]
        
        curr = a

      # Calculate what y and z is based on the a and b 
      d = K - 2**n + 1
      # print S
      # print "a,b,d,S[a],S[b]:",a,b,d,S[a],S[b]
      if b < 0: b = 0
      
      if S[a] >= d:
        y = a
      else:
        y = b

      if 2**n + d <= S[a]:
        z = a
      else:
        z = b




    return y, z

T = int(raw_input())  # read a line with a single integer
for tt in xrange(1, T + 1):
  N, K = [int(s) for s in raw_input().split(" ")] 
  y, z = solve(N, K)
  print "Case #{}: {} {}".format(tt, y, z)