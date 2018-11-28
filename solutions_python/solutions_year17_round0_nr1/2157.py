def ranges_minus(a_original, b_original):
    a = sorted(a_original)
    b = sorted(b_original)
    res = []
    ia = 0
    ib = 0
    while ia<len(a) and ib<len(b):
        if a[ia][0] == a[ia][1]:
            ia += 1
            continue
        elif b[ib][0] == b[ib][1]:
            ib += 1
            continue
        
        if a[ia][0] < b[ib][0] and a[ia][1] <= b[ib][0]:
            res.append((a[ia][0], a[ia][1]))
            ia += 1
        elif a[ia][0] < b[ib][0] and b[ib][0] <= a[ia][1] <= b[ib][1]:
            res.append((a[ia][0], b[ib][0]))
            b[ib] = (a[ia][1], b[ib][1])
            ia += 1
        elif a[ia][0] < b[ib][0] and b[ib][1] < a[ia][1]:
            res.append((a[ia][0], b[ib][0]))
            a[ia] = (b[ib][1], a[ia][1])
            ib += 1
        
        elif b[ib][0] <= a[ia][0] <= b[ib][1] and b[ib][0] < a[ia][1] <= b[ib][1]:
            b[ib] = (a[ia][1], b[ib][1])
            ia += 1
        
        elif b[ib][0] <= a[ia][0] <= b[ib][1] and b[ib][1] < a[ia][1]:
            a[ia] = (b[ib][1], a[ia][1])
            ib += 1
        
        elif b[ib][1] <= a[ia][0]:
            ib += 1
    if ia < len(a):
        for i in range(ia, len(a)):
            res.append(a[ia][:])
    return res
        
            
def ranges_contains_point(ranges, point):
    for r in ranges:
        if r[0] <= point < r[1]:
            return True
        elif point < r[0]:
            return False
    return False

def print_answer(casenum, ans):
    print('Case #{0}: {1}'.format(casenum, ans))

def solve(pancakes, K):
    cnt = 0
    flipped_ranges = []
    size = len(pancakes)
    for i in range(size):
        if ranges_contains_point(flipped_ranges, i):
            pancakes[i] = not pancakes[i]
        if i < size-K+1 and not pancakes[i]:
            pancakes[i] = not pancakes[i]
            flipped_ranges = ranges_minus([(i+1, i+K)], flipped_ranges)
            cnt += 1

    if all(pancakes):
        return cnt
    else:
        return 'IMPOSSIBLE'



def main():
    T = int(input())
    for i in range(T):
        S, K = input().split()
        S = list(map(lambda x: x == '+', S))
        K = int(K)
        ans = solve(S, K)
        print_answer(i+1, ans)

if __name__ == '__main__':
    main()