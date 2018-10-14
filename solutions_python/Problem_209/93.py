import math

def solve(N, K, R, H):
    cakesR = zip(R, H)
    # print map(lambda x: 2 * x[0] * x[1], cakesR)
    cakesH = zip(R, H, map(lambda x: 2 * x[0] * x[1], cakesR))
    cakesR.sort(key=lambda x: x[0], reverse=True)
    cakesH.sort(key=lambda x: x[2], reverse=True)
    # print cakesR
    # print cakesH

    ans = 0
    removed = 0
    for i in range(N):
        r, h = cakesR[i]
        now = r ** 2 + h * r * 2
        jumped = False
        # print now
        counter = 1
        for cake in cakesH:
            # print now
            # print cake
            if counter == K:
                break
            if not jumped and cake[0] == r and cake[1] == h:
                jumped = True
                continue
            if cake[0] > r:
                continue
            now += cake[2]
            counter += 1
        if now > ans:
            ans = now
    return ans * math.pi

def main():
    T = input()
    for i in xrange(1, T + 1):
        N, K = map(int, raw_input().strip().split())
        R = []
        H = []
        for j in range(N):
            r, h = map(int, raw_input().strip().split())
            R.append(r)
            H.append(h)
        print 'Case #{0}: {1}'.format(i, solve(N, K, R, H))

if __name__ == '__main__':
    main()
