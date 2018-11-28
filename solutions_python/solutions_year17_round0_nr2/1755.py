def find_tidy(n):
  digits= [int(i) for  i in str(n)]
  if len(digits)==1:
    return str(n)
  current=digits[-1]
  current_pos=len(digits)-1
  while current_pos!=0:
    for i in range(current_pos,-1,-1):
      if digits[i]<=current:
        continue
      else:
        for j in range(i+1, len(digits)):
          digits[j]=9
        digits[i]=digits[i]-1
        break
    current_pos=current_pos-1
    current=digits[current_pos]
  for j,v in enumerate(digits):
    if v!=0:
      break
  return ''.join([str(i) for i in digits[j:]])


def main():
  t = int(raw_input())  # read a line with a single integer
  for i in xrange(1, t + 1):
    n=int(raw_input())
    output=find_tidy(n)
    print "Case #{}: {}".format(i, output)

main()