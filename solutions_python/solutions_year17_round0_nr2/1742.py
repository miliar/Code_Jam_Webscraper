def find_bad(n_st):
    prev = int(n_st[0])
    for i in range(1,len(n_st)):
        if int(n_st[i]) < prev:
            return i
        prev = int(n_st[i])
    return len(n_st)

def solve(n_st):
    while True:
        bad_idx = find_bad(n_st)
        if bad_idx == len(n_st):
            return 'Case #{}: {}'.format(tc, int(''.join(n_st)))
        n_st[bad_idx:] = ['9']*len(n_st[bad_idx:])
        n_st[bad_idx-1] = str(int(n_st[bad_idx-1])-1)

t = int(input())
for tc in range(1,t+1):
    n_st = list(input())
    print(solve(n_st))
