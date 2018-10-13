
def solve(pancakes, flipper):
    count = 0
    for i in range(len(pancakes)):
        if i <= len(pancakes) - flipper:
            if pancakes[i] == '-':
                # flip
                count += 1
                for k in range(i, i+flipper):
                    if pancakes[k] == '+':
                        pancakes[k:k+1] = '-'
                    else:
                        pancakes[k:k+1] = '+'
        else:
            if pancakes[i] == '-':
                return -1
    return count

fin = open("A-large.in", "r")
fout = open("out.txt", "w")

T = int(fin.readline())

for t in range(T):
    line = fin.readline().split(' ')
    pancakes = line[0]
    flipper = int(line[1])
    ans = solve(list(pancakes), flipper)
    if ans >= 0:
        fout.write("Case #%d: %d\n"%(t+1, ans))
    else:
        fout.write("Case #%d: IMPOSSIBLE\n"%(t+1))

fin.close()
fout.close()