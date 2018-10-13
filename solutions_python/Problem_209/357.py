from math import pi

def ample_syrup():
    N, K = map(int, raw_input().strip().split())
    areas = []
    H = [0] * N
    Rs = []
    for i in xrange(N):
        R, H[i] = map(int, raw_input().strip().split())
        Rs.append((R, i))
        areas.append((2 * R * H[i], R, i))
        
    areas.sort(reverse=True)
    Rs.sort(reverse=True)
    result, total = 0, 0
    for i in xrange(N-K+1):
        total, k = Rs[i][0] * Rs[i][0] + 2 * Rs[i][0] * H[Rs[i][1]], 1
        for j in xrange(N):
            if k == K: break
            if areas[j][1] <= Rs[i][0] and areas[j][2] != Rs[i][1]:
                total += areas[j][0]
                k += 1
        if k == K:
            result = max(result, total)
    return result * pi

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, ample_syrup())