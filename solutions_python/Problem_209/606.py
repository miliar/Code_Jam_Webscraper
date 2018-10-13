import math

def calc(file):
    n, k = map(int, file.readline().split())
    size = [[0,0]]
    for _ in xrange(n):
        size.append( map(int, file.readline().split()))
    size.sort( key=lambda x: x[0])
    ans = [[0]*(k+1) for _ in xrange(n+1)]
    rd = [[0]*(k+1) for _ in xrange(n+1)]
    for i in xrange(1, n+1):
        for j in xrange(1, min(i+1, k+1)):
            ans[i][j] = ans[i-1][j]
            rd[i][j] = rd[i-1][j]
            for r in xrange(i):
                take = ans[r][j-1] + math.pi*size[i][0]*size[i][0] - math.pi*rd[r][j-1]*rd[r][j-1] + 2*math.pi*size[i][0]*size[i][1]
                if take > ans[i][j]:
                    ans[i][j] = take
                    rd[i][j] = size[i][0]

    return ans[n][k]

def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        ans = calc(file)
        fl_o.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    fl_o.close()

main()