fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
T = int(fin.readline())
for cID in range(T):
    print(cID)
    N, K = fin.readline().strip().split()
    N = int(N)
    K = int(K)
    c = 1
    m = N
    inside = 0
    while c < K - inside:
        inside += c
        c = c * 2
        m = m // 2
    left = N - inside

    ex = left - (left // c) * c
    if ex >= K - inside:
        a = (left // c + 1) // 2
        b = (left // c + 1) - a - 1
    else:
        a = (left // c)//2
        b = left // c - 1 - a
    fout.write("Case #{}: {} {}\n".format(cID+1, max(a,b), min(a,b)))