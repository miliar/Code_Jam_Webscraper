
def calc():
    D, N = map(int, raw_input().split())
    mx = 0
    for b_i in xrange(N):
        Ki, Si = map(float, raw_input().split())
        time = float(D - Ki) / Si
        if time > mx:
            mx = time
    return D/mx

T = int(raw_input())

for a_i in xrange(T):

    ans = "Case #{}: {}".format(a_i+1, calc())
    print ans
