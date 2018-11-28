

def Tidy(number):
  return rTidy([int(c) for c in str(number)], [])
  
def rTidy(numlist, result):
  """ base case, we are done """
  if len(numlist) == 0:
    return int("".join([str(c) for c in result]))
  
  last_digit = 9
  if len(result)>0:
    last_digit = result[0]
  next_digit = numlist[-1]

  """ this only happens when we carry numbers over... """
  if next_digit < 0:
    return rTidy(numlist[:-2] + [numlist[-2]-1, 9], result)

  """ num ordered properly """
  if last_digit >= next_digit:
    return rTidy(numlist[:-1], [next_digit] + result)
    
  """ we need to get the largest trailing ints before this """
  return rTidy(numlist[:-1] +[next_digit-1], [9]*len(result))

def Parse():
  fin = open(r"D:\Projects\Python\Google\B-large.in", 'r')
  fout = open(r"D:\Projects\Python\Google\B-large.out", 'w')
  count = int(fin.readline())
  for i in range(1, count+1):
    number = int(fin.readline())
    ret = Tidy(number)
    result = "Case #%d: %s\n" % (i, ret)
    fout.write(result)
  fin.close()
  fout.close()

Parse()