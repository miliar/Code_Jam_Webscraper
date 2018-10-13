import math

def solve(D, N, K_list, S_list):
    # print D, N 
    # print K_list
    # print S_list
    
    # Find the slowest time to get to D
    t_list = []
    for i in range(N):
        t_list.append(float(D - K_list[i])/S_list[i])
    
    # print t_list
    max_t = max(t_list)
    max_t_index = t_list.index(max_t)

    # Calculate the speed
    speed = (float(D)/max_t)

    return speed

T = int(raw_input())  # read a line with a single integer
for tt in xrange(1, T + 1):
  D, N = [int(s) for s in raw_input().split(" ")]
  K_list = []
  S_list = []
  for n in range(N):
    K, S = [int(s) for s in raw_input().split(" ")]
    K_list.append(K)
    S_list.append(S)
  
  ans = solve(D, N, K_list, S_list)
  print "Case #{}: {}".format(tt, ans)