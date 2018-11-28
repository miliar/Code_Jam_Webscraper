def test(r, t, nCase):
    minn = 0
    maxn = t
    while maxn >= minn:
        mid = (minn+maxn)/2
        ml = mid*((2*(r+mid))-1)
        mlnext = (mid+1)*((2*(r+mid+1))-1)
        if mlnext <= t:
            minn = mid+1
        elif ml > t:
            maxn = mid-1
        else:
            print 'Case #' + str(nCase) + ':', mid
            break

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        line = raw_input().split(' ')
        r, t = int(line[0]), int(line[1])
    	test(r, t, i + 1)

