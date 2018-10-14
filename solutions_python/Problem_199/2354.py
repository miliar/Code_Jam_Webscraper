def solve(S,K):
    result = 0
    # print S,K
    for i in range(len(S)):
        # print S[i]
        if (S[i] == "-"):
            if (i + K > len(S)):
                return -1
            result += 1
            for j in range(K):
                if (S[i+j] == '-'):
                    S[i+j] = "+"
                else:
                    S[i+j] = "-"
            # print S
    return result

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  S, K = raw_input().split(" ") # read a list of integers, 2 in this case
  S = list(S)
  K = int(K)
  result = solve(S,K)
  if result == -1:
      print "Case #{}: {}".format(i, "IMPOSSIBLE")
  else:
      print "Case #{}: {}".format(i, result)