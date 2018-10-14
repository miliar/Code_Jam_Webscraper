t = int(input())

for i in range(1, t + 1):
  impossible = False
  changes = 0
  inp = input()
  n, m = inp.split(" ")
  m = int(m)
  n_split = list(n)
  for j in range (0, len(n_split)):
      #print("j:" + str(j) + ":" + n_split[j])
      if n_split[j] == '+':
          continue
      else:
          changes = changes + 1
          if j+m > len(n_split):
              impossible = True
              break
          for k in range(j,j+m):
              #print("k:"+ str(k) +":" + n_split[k])
              if n_split[k] == '-':
                n_split[k] = '+'
              else:
                n_split[k] = '-'
              #print("k_new:"+ str(k) +":" + n_split[k])
                

  if(impossible == True):
    print("Case #{}: IMPOSSIBLE".format(i))
  else:
    print("Case #{}: {}".format(i, changes))
  # check out .format's specification for more formatting options
