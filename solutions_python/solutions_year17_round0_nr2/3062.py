t = int(raw_input())
for _ in range(t):
    num = raw_input()
    for i in range(len(num) - 1)[::-1]:
        if num[i] > num[i + 1]:
            num = num[:i] + (str(int(num[i]) - 1)) + '9' * (len(num) - i - 1)
    print 'Case #' + str(_ + 1) + ': ' +  str(int(num))
