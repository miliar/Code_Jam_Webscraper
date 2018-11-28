f = open('in', 'r')
fout = open('out', 'w')
t = int(f.readline())

def correct(num):
    for k, v in enumerate(num[:-1]):
        if num[k + 1] < v:
            return False
    return True

for casenum in range(1, t + 1):
    num = f.readline().split()
    num = (num[0])

    if len(num) == 1:
        ans = num
    else:
        ans = num
        while not correct(num):
            for k, v in enumerate(num[:-1]):
                if num[k+1] < v:
                    # if k == 0:
                    #     pass
                    ans = num[:k]
                    ans += str(int(v)-1)
                    ans += ''.join(['9'] * len(num[k+1:]))
                    num = ans

    if ans[0] == '0':
        ans = ans[1:]
    fout.write("Case #{}: {}\n".format(casenum, ans))