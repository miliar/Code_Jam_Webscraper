f = open('A-large.in', 'r')
outfile = open('A-large.out', 'w')

T = f.readline()

def getnumber(n):
  s = n
  digit = 1
  map1 = {}
  st = ""
  flag = 1
  for i in s:
    if map1.has_key(i) == False:
      if digit < 10:
        map1[i] = digit
        st = st + str(digit)
        digit = digit+1 
      else:
        map1[i] = digit
        st = st + str(chr(digit))
        digit = digit+1
        
    else:
      st = st + str(map1[i])
    if flag == 1 and digit == 2:
      digit = 0
      flag = 2
    elif flag == 2 and digit == 1:
      digit = 2
      flag = 3
    if digit == 10:
      digit = 97
    
  return st

def maxd(n):
  max = 0
  for i in n:
    if i.isalpha():
      if max < (ord(i)-87):
        max = (ord(i)-87)
    else:
      if max < int(i):
        max = int(i)
  return max

def Nbase10(n, base):
  return int(n, base )

for i in range(1, int(T)+1):
  n = getnumber(f.readline().strip())
  base = maxd(n)+1
  
  outfile.write("Case #" + str(i)+": " + str(Nbase10(n , base)) +"\n")
  #print("Case #" + str(i)), str(Nbase10(n , base)) 
  
outfile.close()
