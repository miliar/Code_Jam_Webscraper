numtests = int(raw_input())
numarr = []
for i in range(numtests):
  numarr.append(int(raw_input()))

def make_tidy(x):
  digits = []
  while(x!=0):
    digits.append(x%10)
    x /= 10
  digits.reverse()
  lendigits = len(digits)
  while(sorted(digits)!=digits):
    for i in range(lendigits-1):
      if(digits[i] > digits[i+1]):
        digits[i] -= 1
        for y in range(i+1,lendigits):
          digits[y] = 9
  return int(''.join(map(str,digits)))
  
for number in range(len(numarr)):
  print 'Case #'+str(number+1)+': '+str(make_tidy(numarr[number]))
