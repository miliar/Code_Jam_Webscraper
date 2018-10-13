def all_not_class(s, _cl='aeiou'):
    return len(s) == len(s.translate(None, _cl))

for case in range(1,input()+1):
    string, n = raw_input().split()
    n = int(n)
    # find consecs
    L = len(string)
    idx_last = L-n+1
    last = -1
    nval = 0
    for i in range(idx_last):
        sub = string[i:i+n]
        if all_not_class(sub):
            nval += (i-last)*(idx_last-i)
            last = i
    print('Case #{0}: {1}'.format(case, nval))
