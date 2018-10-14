def isPalindrome(x):
    x = str(int(x))
    y = x[::-1]
    if x == y:
        return 1
    else:
        return 0
lis = input(': ').split()
if int(lis[0]) * 2 == len(lis) - 1:
    lis.remove(lis[0])
    cases = list(zip( * [iter(lis)] * 2))
    caseNo = 1
    for case in cases:
        noFS = 0
        for a in range(int(case[0]), int(case[1]) + 1):
            if a ** 0.5 == int(a ** 0.5):
                if isPalindrome(a) == 1 and isPalindrome(a ** 0.5) == 1:
                    noFS += 1
        print('Case #' + str(caseNo) + ': ' + str(noFS))
        caseNo += 1
else:
    print('Error: Input not of correct size')
