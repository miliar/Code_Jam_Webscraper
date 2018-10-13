import sys

input = sys.stdin

def solve(S,k):
  S = list(S)
  count = 0
  for i in range(len(S)-k+1):
    if S[i]=='-':
      for j in range(k):
        S[i+j] = '-' if S[i+j]=='+' else '+'
      count+=1
  for j in range(k):
    if S[-j]=='-':
      return 'IMPOSSIBLE'
  return count  

for case in range(int(input.readline())):
      values = input.readline().split()
      print("Case #"+ str(case+1) +":", solve(values[0],int(values[1])))
  
