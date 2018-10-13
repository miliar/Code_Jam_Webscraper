input = open('input.in', 'r')
output = open('output.txt', 'w')
cases = int(input.readline())

def check(s,m):
  if s == 0 and m > 0:
    return 0
  elif 3*m - 2 <= s:
    return 1
  else:
    return 0
    
def surprise(s,m):
  if s == 0 and m > 0:
    return 0
  elif 3*m - 4 <= s:
    return 1
  else:
    return 0

for x in range(cases):
  inword = input.readline().replace('\n','')
  googlers, surp, min = inword.split(' ')[:3]
  scores = inword.split(' ')[3:]
  result = 0
  rem = []
  for y in range(int(googlers)):
    if check(int(scores[y]),int(min)) == 1:
      result += 1
      rem.append(y)
  for y in range(len(rem)):
    scores.pop(rem[(y+1)*-1])
  
  for y in range(int(surp)):
    remo = -1
    for z in range(len(scores)):
      if surprise(int(scores[z]),int(min)) == 1:
        result +=1
        remo = z
        break
    if remo > -1:
      scores.pop(remo)
    
  output.write('Case #' + str(x+1) + ': ' + str(result) + '\n')
  