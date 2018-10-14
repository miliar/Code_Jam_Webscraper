import math, sys

def checkPalin(num):
  numstring = str(num)
  return numstring == numstring[::-1]

def main():
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  ip = open(input_file, 'rU')
  casenums = int(ip.readline())
  solution = ''
  for case in range(1,casenums+1):
    solution = solution + 'Case #'+str(case)+": "
    low,high=map(int, ip.readline().split())
    fnsq = 0
    sqrt_low = int(math.sqrt(low))
    sqrt_high = int(math.sqrt(high))
    for num in range(sqrt_low,sqrt_high+1):
      check_sqrt = checkPalin(num)
      num_sqr = num*num
      check_sqr = checkPalin(num_sqr) and (low<=num_sqr<=high)
      if check_sqrt and check_sqr:
        fnsq += 1
    solution = solution + str(fnsq) + '\n'
  ip.close()
  op = open(output_file, 'w')
  op.write(solution)
  op.close()
  
if __name__ == '__main__':
  main()
