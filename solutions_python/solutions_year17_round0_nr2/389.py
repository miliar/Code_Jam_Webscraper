def is_tidy(num):
    prev = 0
    for digit in num:
        if int(digit) < prev:
            return False
        prev = int(digit)
    return True
 
def last_tidy(N):
    num = str(N)

    while not is_tidy(num):
        n = len(num)
        j = 0
        prev = 0
        for i in range(n):
            if int(num[i]) < prev:
                j = i - 1
                break
            prev = int(num[i])

        result = ''
        result = num[:j] + str(int(num[j]) - 1)
        if j + 1 < n:
            for i in range(j + 1, n):
                result += '9'
        num = result
        
    return int(num)
    

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    print("Case #{}: {}".format(i, last_tidy(N)))
