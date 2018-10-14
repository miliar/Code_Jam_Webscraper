

def pancakes():
  f = open("input_large.txt", "r")
  text  = f.readlines()

  first = text[0].rstrip('\n').split(' ')
  T = int(first[0])

  case = 1
  for i in range(T):
      split = text[case].rstrip('\n').split(' ')
      inp = split[0]
      K = int(split[1])
      a = [0]*len(inp)
      idx = 0
      count = 0
      for c in inp:
          if c == '-':
              count += 1 
              a[idx] = 0
          else:
              a[idx] = 1
          idx += 1
      
      j = 0
      num_flips = 0
      for j in range(len(a) - K + 1):
          if a[j] == 0:
              for k in range(K):
                  a[j+k] = int(not a[j+k])
              num_flips += 1

      bad = False
      for l in range(len(a)):
          if a[l] != 1:
              bad = True

      if bad:
          a.reverse()
          j = 0
          num_flips = 0
          for j in range(len(a) - K + 1):
              if a[j] == 0:
                  for k in range(K):
                      a[j+k] = int(not a[j+k])
                  num_flips += 1

          bad = False
          for l in range(len(a)):
              if a[l] != 1:
                  bad = True

      if bad:
          num_flips = "IMPOSSIBLE"
      
      print "Case #{}: {}".format(case, num_flips)
      case += 1

pancakes()
