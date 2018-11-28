import sys

def solve_test(inp):
    n = inp.readline().strip()
    digits = [0] + [int(x) for x in list(n)]
    last_digit = -1
    for i in range(1, len(digits)):
      if digits[i] < digits[i-1]:
        digits[i-1] -= 1
        k = i-1
        while digits[k] < digits[k-1]:
          digits[k-1] -= 1
          k -= 1
        for j in range(k+1, len(digits)):
          digits[j] = 9
        break
    return str(int(''.join(str(x) for x in digits))) 

inp = open(sys.argv[1])
out = open(sys.argv[1].rsplit('.',1)[0]+'.out', 'w')
n_tests = int(inp.readline())
for i in range(n_tests):
    ans = solve_test(inp)
    print("Case #%d: " % (i+1) + ans, file=out)
out.close()