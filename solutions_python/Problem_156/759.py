fin = open("input.txt", 'r')
fout = open("output.txt", 'w')
t = int(fin.readline())
min_time = 10**9 + 7
def eat(list_, time):
    m = max(list_)
    global min_time
    if m <= 3:
        min_time = min(min_time, time + m)
        return
    eat([list_[i] - 1 for i in range(len(list_))], time + 1)
    cp = list_
    for i in range(len(cp)):
        if cp[i] == m:
            for j in range(m//3, m // 2 + 1):
                eat(cp[:i] + [j] + cp[i + 1:] + [m - j], time + 1)
            break
for test in range(1, t + 1):
    print(test, '==============================')
    d = int(fin.readline())
    k = list(map(int, fin.readline().split()))
    min_time = 10**9+7
    eat(k, 0)
    fout.write('Case #' + str(test) + ': ' + str(min_time) + '\n')
fin.close()
fout.close()
