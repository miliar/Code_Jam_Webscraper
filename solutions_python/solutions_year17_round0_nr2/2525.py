# def solve(n):
#     for i in range(n,-1,-1):
#         ln = map(int, str(i))
#         flag = 0
#         for j in range(len(ln)-1):
#             if ln[j] > ln[j+1]:
#                 flag = 1
#                 break
#         if not flag:
#             return i
#     return 0

# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#   n = int(raw_input())
# #   n = list(n)
# #   n = map(int, n)
#   result = solve(n)
#   print "Case #{}: {}".format(i, result)

def solve(n):
    for i in range(len(n)-1,0,-1):
        for j in range (i,-1,-1):
            if n[j] > n[i]:
                # print i, n[i]
                # print j, n[j]
                n[j] -= 1
                # print range(j+1, i+1)
                for k in range(j+1,len(n)):
                    # print k
                    n[k] = 9
                break

    #   if (n[i] < n[i-1] or n[i] <= 0):
    #       n[i] = 9
    #       n[i-1] -= 1
    result = ""
    for digit in n:
        result += str(digit)
    return result.lstrip("0")

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = raw_input()
  n = list(n)
  n = map(int, n)
  result = solve(n)
  print "Case #{}: {}".format(i, result)