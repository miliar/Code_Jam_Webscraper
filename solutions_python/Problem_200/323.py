import sys

input = sys.stdin

def solve(S):
  top = int(S[0])
  lowpref = '' if top == 1 else str(top-1)
  highpref = str(top)
  i = 1
  while i<len(S) and int(S[i])>= top:
    if int(S[i])==top:
      top = int(S[i])
      lowpref = lowpref + '9'
      highpref = highpref+str(top)
    else:
      top = int(S[i])
      lowpref = highpref+str(top-1)
      highpref = highpref+str(top)
    i+=1
  if i==len(S): return highpref  
  while i< len(S):
    lowpref += '9'
    i+=1
  return lowpref  

for case in range(int(input.readline())):
      values = input.readline().split()
      print("Case #"+ str(case+1) +":", solve(list(values[0])))
  
