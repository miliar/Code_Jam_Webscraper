import math

def calc(file):
    n, k = map(int, file.readline().split())
    u = float(file.readline())
    ps = map(float, file.readline().split())
    ps.append(1.0)
    ps.sort()
    for i in xrange(n):
        diff = ps[i+1]-ps[i]
        rec = diff*(i+1)
        if rec > u:
            allot = u/(i+1)
            for j in xrange(i+1):
                ps[j] += allot
            break
        for j in xrange(i + 1):
            ps[j] += diff
        u -= rec
    ans = 1
    for p in ps:
        ans *= p
    return ans

def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        ans = calc(file)
        fl_o.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    fl_o.close()

main()