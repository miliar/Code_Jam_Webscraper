def is_ascending(s):
    for i in range(1, len(s)):
        if int(s[i]) < int(s[i-1]):
            return False
    return True

for t in range(1, int(input()) + 1):
    n = input()
    if is_ascending(n):
        print('Case #{:d}: {:s}'.format(t, n))
    elif int(n) < int('1'*len(n)):
        print('Case #{:d}: {:s}'.format(t, '9'*(len(n) - 1)))
    else:
        n = list(n)
        for i in range(1, len(n)):
            if int(n[i]) < int(n[i - 1]):
                n[i-1] = str(int(n[i-1])-1)
                for j in range(i, len(n)):
                    n[j] = '9'
                print('Case #{:d}: {:s}'.format(t, ''.join(n)))
                break
