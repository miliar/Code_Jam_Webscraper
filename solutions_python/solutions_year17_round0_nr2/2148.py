
T = int(raw_input())

outp_format = "Case #{}: {}"

def find_last_pretty(n):
    n_arr = list(str(n))
    l = len(n_arr)
    if l == 1:
        return n
    for _ in xrange(l-1):
        if n_arr == sorted(n_arr):
            break
        for i in xrange(l-1):
            
            if n_arr[i] > n_arr[i+1]:
                n_arr[i] = str(int(n_arr[i]) - 1)

                for i2 in xrange(i+1, l):
                    n_arr[i2] = '9'
                else:
                    break
    return int("".join(n_arr))

for i in xrange(T):
    n = int(raw_input())
    ans = find_last_pretty(n)
    print outp_format.format(i+1, ans)