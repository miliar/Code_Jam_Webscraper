def quater(a, b, sign): # sign is int
  dic = {'11': '1', '1i': 'i', '1j': 'j', '1k': 'k',
       'i1': 'i', 'j1': 'j', 'k1': 'k',
       'ij': 'k', 'jk': 'i', 'ki': 'j'}
  result = ''
  if a == 'i' and b == 'i':
    result = '1'
    sign = -sign
  elif a == 'j' and b == 'j':
    result = '1'
    sign = -sign
  elif a == 'k' and b == 'k':
    result = '1'
    sign = -sign
  elif a == 'j' and b == 'i':
    result = 'k'
    sign = -sign
  elif a == 'k' and b == 'j':
    result = 'i'
    sign = -sign
  elif a == 'i' and b == 'k':
    result = 'j'
    sign = -sign
  else:
    result = dic[a+b]
  return [result, sign]

def evaluate(s, sign=1):
  while len(s) > 1:
    r = quater(s[0],s[1],sign)
    s = r[0] + s[2:]
    sign = r[1]
  return [s, sign]

def Dijkstra(s, sign = 1):
  deter = evaluate(s)

  if len(s) < 3:
    return "NO"
  elif ('j' not in s) and ('k' not in s):
    return "NO"
  elif ('k' not in s) and ('i' not in s):
    return "NO"
  elif ('i' not in s) and ('j' not in s):
    return "NO"
  else:
  
    NoI = True
    NoJ = True
    NoK = True
    while len(s) > 0 and NoI:
##      print(s, sign ,'I')
      if s[0] == 'i':
        s = s[1:]
        NoI = False
      elif len(s) >= 2:
        r = quater(s[0], s[1], 1)

        if r[1] == -1:
          sign = -sign
        
        if r == ['i', 1]:
          s = s[2:]
          NoJ = False
  
      if len(s) >= 2 and NoI:
        s = r[0] + s[2:]
      elif len(s) == 1:
        break

    while len(s) > 0 and NoJ:
##      print(s, sign, 'J')
      if s[0] == 'j':
        s = s[1:]
        NoJ = False
      elif len(s) >= 2:
        r = quater(s[0], s[1], 1)
        if r[1] == -1:
          sign = -sign
        if r == ['j', 1]:
          s = s[2:]
          NoJ = False
      if len(s) >= 2 and NoJ:
        s = r[0] + s[2:]
      elif len(s) == 1:
        break
          
        
    while len(s) > 0 and NoK:
##      print(s, sign, 'K')
      if s[0] == 'k':
        s = s[1:]
        NoK = False
      elif len(s) >= 2:
        r = quater(s[0], s[1], 1)
        if r[1] == -1:
          sign = -sign
        if r == ['k', 1]:
          s = s[2:]
          NoK = False
      if len(s) >= 2 and NoK:
        s = r[0] + s[2:]
      elif len(s) == 1:
        break

    if deter != ['1', -1]:
      return "NO"
    elif (NoI == False) and (NoJ == False) and (NoK == False):
      return "YES"
    else:
      return "NO"

  


infile = open("C-small-attempt1.in", 'r')
lines = infile.readlines()
T = int(lines[0].rstrip())

outfile = open("C-small-1.out", 'w')

for i in range(T):
  LX = lines[2*i+1].rstrip().split(" ")
  L = int(LX[0])
  X = int(LX[1])
  S = lines[2*i+2].rstrip()
  quain = S*X
  outfile.write("Case #{0}: {1}".format(i+1,Dijkstra(quain)))
  outfile.write("\n")

outfile.close()
infile.close()
  

  














