input = open('input.in', 'r')
output = open('output.txt', 'w')
cases = int(input.readline())

def check(x,y):
  res = 0
  for i in range(len(str(x))-1):
    if str(x)[-(i+1):] + str(x)[:-(i+1)] == str(y):
      return 1
      break
      res = 1
  if res == 0:
    return 0

for x in range(cases):
  inword = input.readline().replace('\n','')
  A, B = inword.split(' ')
  result = 0
  for n in range(int(A),int(B)):
    for m in range(n+1,int(B)+1):
      if check(n,m) == 1:
        result += 1
  
  output.write('Case #' + str(x+1) + ': ' + str(result) + '\n')