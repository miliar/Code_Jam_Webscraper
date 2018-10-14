import sys

if __name__ == '__main__':
    s = sys.stdin.readline()

    for x in range(1, int(s) + 1):
        sum = 0
        line = sys.stdin.readline()
        r, k, n = line.split()
        r = int(r)
        k = int(k)
        n = int(n)
        
        g = sys.stdin.readline().split()
        for i in range(0, len(g)):
            g[i] = int(g[i])

        j = 0
        while r > 0:
            sub_sum = 0
            other_count = 1
            while k - sub_sum >= g[j] and other_count <= len(g):
                sub_sum += g[j]
                j += 1
                j = j % len(g)
                other_count += 1
            sum += sub_sum
            r -= 1


        print("Case #%d: %d" % (x, sum))
