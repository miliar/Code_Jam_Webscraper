def solve(Nstr):
  res = ''
  numToDecrement = -1 # invalid value
  for i in range(len(Nstr) - 1): # loop from 0 to len(Nstr) - 2
    if (Nstr[i+1] < Nstr[i]): # next digit less than previous digit
      numToDecrement = Nstr[i]
      break;
  if numToDecrement == -1: # string is already arrange in non descending order
    return Nstr
  #print numToDecrement
  flag = False; # it will be true after first most significant occurance of numToDecrement
  for i in Nstr:
    if flag == False and i == numToDecrement:
      flag = True
      res += str(int(numToDecrement) - 1)
    elif flag:
      res += '9'
    else:
      res += i
  return long(res)

T = int(input())  
for i in range(1, T + 1):
  N = raw_input()
  print("Case #{}: {}".format(i, solve(N)))
