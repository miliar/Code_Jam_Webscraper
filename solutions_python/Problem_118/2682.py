import sys, math

def _sqr(num):
    xi = float(num)/2
    xk = xi
    tolerance = 0.00000005
    while True:
        xi = xk
        xk = xi - ( float(xi*xi - num) / (2*xi))
        if (abs(xk-xi) < tolerance):
            break
    return int(xk) if xk.is_integer() else xk 

def is_palindrome(num):
    num = int(num) if float(num).is_integer() else num
    num = str(num).replace('.','')
    while num:
      if num[:1] != num[-1:]:
          return False
      num = num[1:-1]
    return True

def fair_and_square(num):
    #sqr = _sqr(num)
    sqr = math.sqrt(num)
    if not is_palindrome(num):
        return 0
    if not is_palindrome(sqr):
        return 0
    return 1
     
def main():
    test_case = int(sys.stdin.readline())
    for i in xrange(1, test_case+1):
        a,b = map(int, sys.stdin.readline().split())
        count = sum(fair_and_square(num) for num in xrange(a, b+1))
        print('Case #%d: %i' %  (i, count)) 

if __name__=='__main__':
    main()
