
def is_tidy(N):
    return N == sorted(N)

def index_untidy(N):
    for i in range(len(N)):
        if not is_tidy(N[:i+1]):
            return i
   # return len(N)

def index_eq(N):
    for i in range(len(N)):
        if N[i] == N[-1]:
            return i

def pr(N):
    res = ''
    for n in N:
        res =  res + str(n)
    return str(int(res))
    return res


def search_tidy(N):
    if is_tidy(N):
        return pr(N)
    i = index_untidy(N)-1
    if i<len(N):
        N = N[:i] + [N[i]-1] + [9] * (len(N)-i-1)
    return search_tidy(N)


T = int(input().strip())
for t in range(T):
    N = list(map(int, input().strip()))
    print('Case #'+str(t+1)+': '+search_tidy(N))
