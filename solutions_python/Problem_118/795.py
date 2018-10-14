import math

def is_fair(n):
  s = str(n)
  ret = True
  for i in range(len(s)/2):
    if s[i] != s[-(i+1)]:
      ret = False
      break
  return ret  

def build_odd_digits(ndigits, curNDig, pos, n, fair_and_square):
  centerPos = curNDig/2
  small = pow(10, centerPos-pos)
  large = pow(10, centerPos+pos)
  for i in range(0,10):
    if curNDig == 1:
      new_n = n + i*small
    else:  
      new_n = n + i*small + i*large

    if i:
      n2 = new_n*new_n
      if is_fair(n2):
        fair_and_square.append(n2)
    if curNDig < ndigits:
      build_odd_digits(ndigits, curNDig+2, pos+1, new_n*10, fair_and_square)

  return    

def build_even_digits(ndigits, curNDig, pos, n, fair_and_square):
  centerPos = curNDig/2

  small = pow(10, centerPos-pos-1)
  large = pow(10, centerPos+pos)

  for i in range(0,10):
    new_n = n + i*small + i*large
    if i:
      n2 = new_n*new_n
      if is_fair(n2):
        fair_and_square.append(n2)
    if curNDig < ndigits:    
      build_even_digits(ndigits, curNDig+2, pos+1, new_n*100, fair_and_square)
      
  return    

def build_fair_and_square(ndigits, fair_and_square):
  ndigits = ndigits/2
  if ndigits%2:
    build_odd_digits(ndigits,1,0,0, fair_and_square)
    build_even_digits(ndigits+1,2,0,0, fair_and_square)
  else:
    build_even_digits(ndigits,2,0,0, fair_and_square)
    build_odd_digits(ndigits+1,1,0,0, fair_and_square)
  return
    

def solve(fIn, fair_and_square):
  result = 0
  line = fIn.readline()
  [a, b] = [int(x) for x in line.split()]

  for n in fair_and_square:
    if a<=n and b>=n:
      result += 1
    if b<n:
      break
  return result

def main(filename,ndigits):
  fair_and_square = []

  fIn = open(filename)
  fOut = open(filename+'.out', 'w')
  build_fair_and_square(ndigits, fair_and_square)
  fair_and_square=sorted(fair_and_square)
  print "main : ", fair_and_square
  numTestCases=int(fIn.readline())
  for i in range(numTestCases):
    result = solve(fIn,fair_and_square)
    fOut.write('Case #' + str(i+1) + ': ' + str(result) + '\n')

  fIn.close()
  fOut.close()
  return
    

main('D:\\tech\\code_jam\\2013\\Problem C. Fair and Square\\C-small-attempt0.in', 4)


