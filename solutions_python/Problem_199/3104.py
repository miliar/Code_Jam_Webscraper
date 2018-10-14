from math import inf

def count(s,k):
    for i in range(len(s)):
        if s[i] == '-':
            if len(s)-i < k:
                return inf
            for j in range(i, i+k):
                s[j] = '+' if s[j] == '-' else '-'
            for j in range(i, len(s)):
                if s[j] == '-':
                    return 1+count(s,k)
            return 1
    return 0

if __name__ == '__main__':
    import sys,re
    data = iter(sys.stdin.read().splitlines())
    next(data)
    
    for (case_num, case) in enumerate(data):
        s,k = case.split()
        s = list(s); k = int(k)
        res = count(s,k)
        if res == inf:
            res = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(case_num+1, res))
