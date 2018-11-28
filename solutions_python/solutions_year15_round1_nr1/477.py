def first_count(array):
    ans = 0
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            ans += array[i-1] - array[i]
    return ans


def second_count(array):
    n = len(array)
    v = [array[i-1] - array[i] for i in range(1, n)]
    v_min = max(v)
    ans = 0
    for i in range(n-1):
        ans += min(array[i], v_min)
    return ans

T = int(raw_input())

for i in range(T):
    N = raw_input()
    m = map(int, raw_input().split(" "))
    print "Case #%i: %i %i" % (i+1, first_count(m), second_count(m))
