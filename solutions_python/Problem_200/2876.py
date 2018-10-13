def is_tidy(strnum):
    return strnum == ''.join(sorted(strnum))

def last_tidy(strnum):
    num = int(strnum)
    while not is_tidy(str(num)):
        num -= 1
    return num

t = int(raw_input())
for case in range(t):
    n = raw_input()
    print 'Case #{}: {}'.format(case + 1, last_tidy(n))
