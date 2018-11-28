import sys, os, re, collections, heapq, math, itertools

def print_result (case_num, result):
    print('Case #{}: {}'.format(case_num + 1, result))

def IsApproximatelyEqual(x, y, epsilon):
    """Returns True iff y is within relative or absolute 'epsilon' of x.

    By default, 'epsilon' is 1e-6.
    """
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return (-epsilon <= (x - y) / x <= epsilon \
            or -epsilon <= (x - y) / y <= epsilon)



def get_area (r,h):
    return 2 * math.pi * r * h

def get_top_area (r):
    return math.pi * r**2

def try_one (K, pancakes, largest_r):
    n_pancakes = [(r,h) for r,h in pancakes if r <= largest_r]
    if len(n_pancakes) < K-1:
        return -1
    n_pancakes.sort(key=lambda a:get_area(*a),reverse=True)
    assert len(n_pancakes[:K-1]) == K-1
    return sum([get_area(r,h) for r,h in n_pancakes[:K-1]])

def solve (K,pancakes):
    if K == 1:
        lowest = max(pancakes,key=lambda b:get_top_area(b[0]) + \
                get_area(b[0],b[1]))
        #print('s1',lowest,file=sys.stderr)
        return get_top_area(lowest[0]) + get_area(*lowest)
    maxa = 0
    for i in range(len(pancakes)):
        lowest = pancakes[i]
        n_pancakes = pancakes[:i] + pancakes[i+1:]
        assert len(n_pancakes) == len(pancakes) - 1
        area = try_one(K,n_pancakes,lowest[0]) + \
                get_top_area(lowest[0]) + get_area(*lowest)
        maxa = max(maxa,area)
    return '{:20.50}'.format(maxa).lstrip()

def solve2 (K,pancakes):
    maxa = 0
    mm = None
    for comb in itertools.combinations(pancakes,K):
        candidate = sorted(comb,key=lambda a:a[0],reverse=True)
        a = get_top_area(candidate[0][0]) + \
            sum([get_area(r,h) for r,h in candidate])
        #maxa = max(a,maxa)
        if maxa < a:
            maxa = a
            mm = candidate
    #print('s2',mm,file=sys.stderr)
    return maxa



def main():
    for case_num in range(int(input())):
        N,K = map(int,input().split())
        pancakes = []
        for _ in range(N):
            r,h = map(int,input().split())
            pancakes.append((r,h))
        r = solve(K,pancakes)
        #r2 = solve2(K,pancakes)
        #assert IsApproximatelyEqual(float(r),float(r2),10**-6), (r,r2,case_num)
        print_result(case_num,r)

if __name__ == "__main__":
    main()
