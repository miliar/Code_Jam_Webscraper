import sys


n = int(raw_input().strip())

for case_num in range(n):
    arr = raw_input().strip().split(' ')
    pancakes = list(arr[0])
    k = int(arr[1])
    step = 0
    for i, ch in enumerate(pancakes):
        if ch == '-' and i <= len(pancakes) - k:
            step += 1
            for j in range(i, i+k):
                if pancakes[j] == '-':
                    pancakes[j] = '+'
                else:
                    pancakes[j] = '-'

    for ch in pancakes:
        if ch == '-':
            print 'Case #{}: IMPOSSIBLE'.format(case_num+1)
            break
    else:
        print 'Case #{}: {}'.format(case_num+1, step)
