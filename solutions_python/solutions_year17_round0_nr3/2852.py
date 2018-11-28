def solve(n, k):
    # Naive approach.
    bathrooms = [0]*n
    for _ in range(k):
        oL = -1
        oR = n
        s = {}
        for i, o in enumerate(bathrooms):
            if o:
                oL = i
            else:
                s[i] = (i-oL-1, 0)
        for i in range(len(bathrooms)-1,-1,-1):
            o = bathrooms[i]
            if o:
                oR = i
            else:
                s[i] = (s[i][0], oR-i-1)
        minLR = max(map(min, s.values()))
        ties = filter(lambda t: min(t[1]) == minLR, s.items())
        i, pair = max(ties, key=lambda t: max(t[1]))
        bathrooms[i] = 1
    return max(pair), minLR
                

def problemC():
    T = int(input())
    for i in range(T):
        n, k = map(int, input().split())
        solution = solve(n, k)
        print('Case #{}: {} {}'.format(i+1, solution[0], solution[1]))

problemC()
