number_of_tests = int(input())

for test_number in range(number_of_tests):
    n = list(input())
    last_i = -1
    for i in range(len(n) - 1):
        if n[i] > n[i+1]:
            last_i = i
            n[last_i] = chr(ord(n[last_i]) - 1)
            for j in range(i+1, len(n)):
                n[j] = '9'
            break
    if last_i >= 0:
        for i in range(last_i, 0, -1):
            if n[i] < n[i-1]:
                n[i] = '9'
                n[i-1] = chr(ord(n[i-1]) - 1)
    print("Case #{}: {}".format(test_number+1, int(''.join(n))))
