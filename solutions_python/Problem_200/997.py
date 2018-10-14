'''
4
132
1000
7
111111111111111110
'''

def is_tidy(x):
    x = str(x)
    if len(x) < 2:
        return True
    for i in range(1, len(x)):
        if x[i-1]>x[i]:
            return False
    return True

T = int(raw_input())
case_number = 1
while case_number <= T:
    n = raw_input()
    while not is_tidy(n):
        for i in range(1, len(n)):
            if n[i] < n[i-1]:
                n = str(int(n[:i]) - 1) + '9'*(len(n)-i)
                if n[0] == '0':
                    n = n[1:]
                break
    print 'Case #{0}: {1}'.format(case_number, n)
    case_number += 1

exit()


# small input


T = int(raw_input())
case_number = 1
while case_number <= T:
    n = int(raw_input())
    while not is_tidy(n):
        n -= 1
    print 'Case #{0}: {1}'.format(case_number, n)
    case_number += 1

