f = open('B-large.in', 'r')
t = int (f.readline())

for c in xrange(1, t + 1):
  result = ""
  digits = list(f.readline().strip())
  i=0
  while (i<(len(digits)-1) and digits[i]<=digits[i+1]):
    i+=1


  if (i < (len(digits)-1)):
    while (i>=1 and digits[i] == digits[i-1]):
      i-=1
    digits[i] = chr(ord(digits[i])-1)
    i=i+1
    while (i<len(digits)):
      digits[i]='9'
      i=i+1

  print "Case #{}: {}".format(c, str(int(''.join(digits))))
