from bisect import bisect_left

def digits(n):
    d = []
    while n > 0:
        d.append(n%10)
        n = int(n/10)
    return list(reversed(d))

def minVal(n, num_digits):
    d = digits(n)
    if len(d) > num_digits:
        raise Exception('Invalid value' + n)
    last_digit = int(n%10)
    val = n
    for i in range(len(d), num_digits):
        val = val*10 + last_digit
    #print('minval for {0} : {1}'.format(n, val))
    return int(val)

def solve(N):
    d = digits(N)
    val = 0
    for i in d:
        val = int(val*10 + i)
        if minVal(val, len(d)) > N:
            val -=1
            #print(val)
            while (val*10+9) < N:
                val = val*10+9
            return int(val)
    return int(val)

def main():
    T = int(input())
    for i in range(1, T+1):
        j = int(input())
        print('Case #{0}: {1}'.format(i, solve(j)))

main()
