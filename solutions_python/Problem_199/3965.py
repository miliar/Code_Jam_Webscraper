def getHappyNum(S):
  count = 0
  for cake in S:
    if cake == '+':
      count += 1
  return count
    
def recur(S, K):
  if getHappyNum(S)==len(S):
    return 0
  elif len(S) < K:
    return -1000
  else:
    if S[0] == '-':
      newS = list(S[1:])
      
      for i in range(K-1):
        if newS[i] == '+':
          newS[i] = '-'
        else:
          newS[i] = '+'
      
      res1 = recur(newS, K)
      
      if res1 == -1000:
        return -1000
      else:
        return res1+1
    else:
      tempRes = recur(list(S[1:]), K)
      return tempRes
 
def findResult(S, K):
  res = recur(list(S),K)
  if res == -1000:
    return 'IMPOSSIBLE'
  else:
    return res

f = open('A-small-attempt0.in', 'r+')
fw = open('result1.txt', 'w+')

lines = f.readlines()
print(lines)
T = int(lines[0])
for i in range(int(T)):
  line = lines[i+1].split()
  S = line[0]
  K = int(line[1])
  
  res = findResult(S, K)
  print('Case #' + str(i+1) + ': ' + str(res))
  fw.write('Case #' + str(i+1) + ': ' + str(res) + '\n')

f.close()
fw.close()