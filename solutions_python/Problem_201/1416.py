from Queue import PriorityQueue
fin = open("C-small-1-attempt0.in")
T = int(fin.readline())
fout = open('C_output.txt', 'w')
for t in range(1, T + 1):
    N, K = fin.readline().strip().split(' ')
    N = int(N)
    K = int(K)
    Q = PriorityQueue()
    Q.put((N, 0, N + 1))
    for i in range(K - 1):
        size, left, right = Q.get()
        mid = (left + right) / 2
        Q.put((-(mid - left - 1), left, mid))
        Q.put((-(right - mid - 1), mid, right))
    size, left, right = Q.get()
    mid = (left + right) / 2
    ls = mid - left - 1
    rs = right - mid - 1
    fout.write("Case #%s: %s %s\n" % (t, max(ls, rs), min(ls, rs)))

fin.close()
fout.close()