from bisect import insort, bisect_left, bisect_right

def palin(x):
    return str(x) == str(x)[::-1]

arr = []

def gen(N):
    for x in range(1, int(N**.5)+1):
        if palin(x) and palin(x*x) and 1 <= x*x <= N:
            insort(arr, x*x)

def solve(A, B):
    l = bisect_left(arr, A)
    r = bisect_right(arr, B)
    return r-l

if __name__ == '__main__':
    gen(10**14)
    T = int(raw_input())
    for case in range(1,T+1):
        A, B = map(int, raw_input().split())
        print "Case #{}: {}".format(case, solve(A, B))
