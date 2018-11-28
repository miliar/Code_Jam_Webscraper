file = open('A-large.in')
out = open('output.txt', 'w')
for t in range(1, int(file.readline())+1):
    N, X = map(int, file.readline().split())
    S = sorted(map(int, file.readline().split()))
    count = 0
    while S:
        if S[-1] + S[0] <= X:
            del S[0]
        if S:
            del S[-1]
        count += 1
    print("Case #%i: %i" % (t, count), file=out)
