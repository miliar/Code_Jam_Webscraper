input = open("input.txt", "r").readlines()
output  = open("output.txt", "w")

def gcd(a, b):
  while a > 0 and b > 0:
    if a > b:
        a = a % b
    else:
        b = b % a
  return a + b

def solve(numbers):
  current = 0
  s = set()
  
  for i in numbers:
    for j in numbers:
      s.add(abs(i - j))

  for x in s:
    current = gcd(current, x)
  T = current
  assert T > 0
  if T <= 1:
    y = 0
  else:
    y = (T - (numbers[0] % T)) % T
  return y

NTest = int(input[0])
for it in range(NTest):
  print it
  parts = input[it + 1].split(" ")
  sz = int(parts[0])
  parts = parts[1:]
  numbers = [int(x) for x in parts]
  assert sz == len(numbers)
  res = solve(numbers)
  output.write("Case #%d: %d\n" % (it + 1, res))

output.close()
  

