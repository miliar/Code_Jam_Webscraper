import math

input =  open("Qualification/C-small-attempt0.in")
output = open("Qualification/C-small-attempt0.out", 'w')

def IsPallindrome(value):
  s = str(value)
  return s == s[::-1]

T = int(input.readline())
for t in range(T):
  print "case",t
  line = input.readline()[:-1]
  A, B = map(int, line.split(" "))
  a = int(math.floor(math.sqrt(A))) 
  b = int(math.ceil(math.sqrt(B)))+1
  count = 0
  for x in range(a,b):
    if x*x < A:
      continue
    if x*x > B:
      break
    if IsPallindrome(x) and IsPallindrome(x*x):
      count += 1
  result = count
  print count
  output.write("Case #{0}: {1}\n".format(t+1, result))

output.flush()
input.close()
output.close()

