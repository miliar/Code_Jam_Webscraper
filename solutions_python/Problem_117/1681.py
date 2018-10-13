import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for tc in range(n):
        a = sys.stdin.readline().split()
        n = int(a[0])
        m = int(a[1])
        a = []
        for i in range(n):
            a.append([x.strip() for x in sys.stdin.readline().split()])
        mxx = []
        mxy = []
        for i in range(n):
            mx = a[i][0]
            for j in range(m):
                mx = max(mx, a[i][j])
            mxx.append(mx)
        for i in range(m):
            mx = a[0][i]
            for j in range(n):
                mx = max(mx, a[j][i])
            mxy.append(mx)
        possible = True
        for i in range(n):
            for j in range(m):
                if a[i][j] < mxx[i] and a[i][j] < mxy[j]:
                    possible = False
        print "Case #" + str(tc + 1) + ": " + ("YES" if possible else "NO")
