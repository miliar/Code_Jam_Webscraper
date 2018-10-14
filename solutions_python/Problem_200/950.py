def checkTidiness(number):
    s = list(str(number))

    if (len(s) < 2):
        return number
    i = 1
    temp = s[0]

    while i < len(s):
        if s[i] >= temp:
            temp = s[i]
            i += 1
        else:
            break

    if i == len(s):
        return number

    s[i - 1] = str(int(s[i - 1]) - 1)

    while i < len(s):
        s[i] = '9'
        i += 1
    return checkTidiness(int(''.join(s)))



t = input()
i = 1
while t:
    t -= 1
    n = input()
    print "Case #" + str(i) + ": " + str(checkTidiness(n))
    i += 1
