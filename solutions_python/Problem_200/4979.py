N = []
with open('b-small.txt') as f:
    T = int(f.readline())
    for case in range(T):
        N.append(int(f.readline()))

with open('answer.txt', 'w') as f:
    for i, case in enumerate(N):
        for n in reversed(range(case+1)):
            str_n = str(n)
            tidy = True
            for idx in range(len(str_n)-1):
                if int(str_n[idx]) > int(str_n[idx+1]):
                    tidy = False
                    break
            if tidy:
                f.write("case #{}: {}\n".format(i+1, n))
                break
