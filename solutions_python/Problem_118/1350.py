import math

def next_palindrome(x, checked=True):
  if x < 9:
    return x+1
  y = list(str(x))
  odd = len(y) % 2 == 1
  mid = len(y)/2 + odd
  length = len(y)
  j = mid
  out = list(y)
  while j > 0:
    if y[j-1] == "9":
      out[j-1] = "0"
      out[-j] = "0"
      j-=1
    else:
      if int(y[-j]) < int(y[j-1]):
        out[-j] = out[j-1]
      else: 
        tmp = str(int(y[j-1]) + 1)
        out[j-1] = tmp
        out[-j] = tmp
      out = ''.join(out)
      break
  if j == 0:
    out = "1"+"0"*(len(y)-1)+"1"
  return int(out)

f = open("C:/Files/GoogleJam/2013/C-small-attempt3.in")
n = int(f.readline().rstrip())
y = open("C:/Files/GoogleJam/2013/C_small_out5.txt", 'w')

i = 1
for i in range(1,n+1):
  x = f.readline().rstrip().split()
  start = int(x[0])
  k=int(math.ceil(pow(start,0.5)))
  end = int(x[1])
  kstart = k
  kend = int(math.floor(pow(end,0.5)))
  num = 0
  isq = pow(k,2)
  while isq <= end:    
    if (str(k)[::-1] == str(k)) and str(isq)[::-1] == str(isq):
      num += 1
    k = next_palindrome(k)    
    isq = pow(k,2)
  y.write("Case #"+str(i)+": "+str(num)+"\n")


y.close()
