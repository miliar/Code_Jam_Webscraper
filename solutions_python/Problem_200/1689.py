def is_tidy(N):
    prev = None
    for c in N:
        if prev is not None and int(c) < prev:
            return False
        prev = int(c)
    return True

def tidy():
  f = open("input_large2.txt", "r")
  text  = f.readlines()

  first = text[0].rstrip('\n').split(' ')
  T = int(first[0])

  case = 1
  for i in range(T):
      split = text[case].rstrip('\n').split(' ')
      N = split[0]
      prev = int(N[0])
      maxN = 9
      maxI = len(N)
      for i,c in enumerate(N):
          cur = int(c)
          if cur < prev:
              i -= 1
              c = N[i]
              while N[i] == c and i >= 0:
                  i -= 1
              
              maxN = cur
              maxI = i+1
              break
          prev = cur

      res = ""
      for i in range(maxI):
          cur = int(N[i])
          res += str(cur)
      if maxI < len(N):
          res += str(int(N[maxI]) - 1)

      for i in range(maxI + 1, len(N)):
          res += "9"
      
      if maxI < len(N) and int(N[maxI]) - 1== 0:
          res = "9"*(len(N) - 1)

      '''
      for l in range(int(N), 0, -1):
          if is_tidy(str(l)):
              if str(l) != res:
                  print "Case #{}: {} {}".format(case, l, res)
                  break
              else:
                  break
      '''
      print "Case #{}: {}".format(case, res)
      case += 1


tidy()
