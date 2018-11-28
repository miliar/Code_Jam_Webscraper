def isValid(A,B,digits,i):
  value = int(digits)
  return (value > i and value <= B)

def value(A,B,i,used):
  result = 0
  digits = str(i)

  for position in range(len(digits)):
    rotated_digits = digits[position:]+digits[:position]
    if(isValid(A,B,rotated_digits,i) and not used.has_key(digits+','+rotated_digits)):
      result += 1
      used[digits+','+rotated_digits] = True
  return result

def process_input(case):
  A,B = [int(element)for element in case.split(' ')]
  result = 0
  used = {}
  for i in xrange(A,B):
    result += value(A,B,i,used)

  return result

def main():
  T = int(raw_input())
  for i in range(1,T+1):
    case = raw_input()
    print "Case #%d: %d"%(i, process_input(case))

if __name__ == '__main__':
  main()