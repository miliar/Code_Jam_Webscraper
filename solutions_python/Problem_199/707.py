f = open('in', 'r')
fout = open('out2', 'w')
t = int(f.readline())

def flip(str, start, k):
    temp = ''
    for i in range(start, start+k):
        if str[i] == '+':
            temp += '-'
        else:
            temp += '+'
    return str[:start] + temp + str[start+k:]

for casenum in range(1, t + 1):
    str, k = f.readline().split()
    k = int(k)
    d = dict()
    d[str] = 0
    q = [str]
    sz = len(str)

    tot = 0
    for start in range(sz - k + 1):
        if str[start] == '-':
            str = flip(str, start, k)
            tot += 1



    target = '+' * sz
    # print target
    if str == target:
        ans = tot
    else:
        ans = 'IMPOSSIBLE'
    fout.write("Case #{}: {}\n".format(casenum, ans))