#!python
def solve(n):
    if n%10 == 0:
        return solve(n-1)
    digits = [int(c) for c in str(n)]
    res = digits[0:1]
    carry = False    
    try:
      for d in range(1, len(digits)):
        if carry:
            res.append(9)
        elif digits[d] >= digits[d-1]:
            res.append(digits[d])
        else:            
            res[-1] -= 1
            i = 1
            while i < len(res) and res[-i] < res[-i-1]:
                res[-i] = 9
                res[-1-1] -= 1
                i += 1                
            res.append(9)
            carry = True            
      res = fix(res)    
      return int(''.join(str(d) for d in res))        
    except:
        return int(''.join('9' for _ in range(len(digits) - 1)))

def fix(digits):
    try:
        i = digits.index(0)
        if i == 0:
            return digits
        else:
            digits[i] = 9
            digits[i-1] -= 1
            return fix(digits)
    except:
        return digits

def main():
    t = int(input())
    for c in range(1, t + 1):
        n = int(input())
        res = solve(n)
        print('Case #%d: %s' % (c, res))
    
if __name__ == "__main__":
  main()
    