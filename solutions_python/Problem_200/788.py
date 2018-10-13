fin = open("B.in")
fout = open("B.out", "w")
T = int(fin.readline())

def done(t, num):
    fout.write("Case #"+str(t+1) + ": " + str(num) + "\n")

for t in range(T):
    num = fin.readline().strip()
    rnum = list(map(int, list(reversed(num))))
    ans = []
    for i in range(len(rnum)-1):
        d = rnum[i]
        if d >= rnum[i+1]:
            ans.append(d)
        else:
            ans.append(9)
            for k, _ in enumerate(ans):
                ans[k] = 9;
            rnum[i+1] -= 1
    ans += [rnum[-1]]
    ans = str(int("".join(map(str, reversed(ans)))))
    done(t, ans)

                

