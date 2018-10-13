
def greatest_lower_tidy_number(n, n_str):
    n_len = len(n_str)
    m = n
    first=True
    """for j in range(n_len-1, -1, -1):
        t = m // 10**j
        print(n, j, t)
        m = n % 10**j
        next = m // 10**(j-1)
        if (t < next):
            for k in range (j, n_len-1):
                t = n % 10**(j+1) // 10**j
                next = (n % 10**j) // 10**(j-1)
                if (t < next):
                    n = n - ((next - t) - 1)*10**(j-1)"""
    digits=[]
    for l in range(n_len-1, -1, -1):
        digits.append(int(n_str[l]))
    digits.append(0)
    for j in range(n_len-1, -1, -1):
        if digits[j+1] > digits[j]:
            digits[j] = 9
            if first:
                digits[j+1] -= 1
                first=False
                for k in range(j+1, n_len-1):
                    if digits[k+1] > digits[k]:
                        if digits[k+1] == 1:
                            digits[k+1] -= 1
                            digits[k] = 9
                        else:
                            digits[k+1] -= 1
                            digits[k] = 9
    re = 0
    for i in range(n_len):
        re += digits[i]*10**i
    """digits=[0]
    for l in range(n_len):
        digits.append(int(n_str[l]))
    print("< ", digits)
    
    for j in range(1, n_len + 1):
        print(n, j, digits[j])
        if digits[j-1] > digits[j]:
            digits[j] = 9
            if first:
                digits[j-1] -= 1
            for k in range(j+1, n_len-1):
                if digits[k+1] > digits[k]:
                    if digits[k+1] == 1:
                        digits[k+1] -= 1
                        digits[k] = 9
                    else:
                        digits[k+1] -= 1
                    print("ups")"""
    return (re)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    #n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    n = input()
    
    res = greatest_lower_tidy_number(int(n), n)
    
    print("Case #{}: {}".format(i, res))

