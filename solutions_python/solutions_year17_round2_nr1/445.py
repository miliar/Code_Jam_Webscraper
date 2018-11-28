def calc(file):
    d, n = map(int, file.readline().split())
    maxtime = 0
    for _ in xrange(n):
        k, s = map(int, file.readline().split())
        dist = (d-k)*1.0
        time = dist/s
        if time > maxtime:
            maxtime = time

    return d/maxtime


def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        ans = calc(file)
        fl_o.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    fl_o.close()

main()