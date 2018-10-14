#!/usr/bin/env python

def get_tidy_num(N):
    if len(str(N)) == 1:
        return N

    new_N = map(int, str(N))
    i = 1
    while i < len(new_N) and new_N[i] >= new_N[i - 1]: 
        i += 1

    if i < len(new_N):
        j = i - 1
        while j >= 0:
            if new_N[j] - 1 >= 0:
                new_N[j] -= 1
            else:
                new_N[j] = 9
            if (j == 0) or (j - 1 >= 0 and new_N[j] >= new_N[j - 1]):
                break
            j -= 1
        j += 1
        while j < len(new_N):
            new_N[j] = 9
            j += 1

    if new_N[0] == 0:
        new_N = new_N[1:]
    return ''.join(map(str, new_N))

if __name__ == '__main__':
    T = int(raw_input())
    for tc in range(1, T + 1):
        N = int(raw_input())
        print 'Case #%d: %s' % (tc, get_tidy_num(N))
