for t in range(1, int(input())+1):
    s, k = input().split()
    s, k, steps = list(s), int(k), 0
    while s:
        if s[0] == '+':
            del s[0]
        else:
            if len(s) < k:
                break
            else:
                steps += 1
                for i in range(k):
                    s[i] = '+' if s[i] == '-' else '-'
        #print(s)
    print('Case #{:d}: {:s}'.format(t, str(steps) if not s else 'IMPOSSIBLE'))
