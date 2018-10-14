t = int(input())
for i in range(1, t + 1):
    curr = [int(d) for d in str(input())]
    while 1:
        fail = 0
        for ch in range(len(curr)-1):
            if curr[ch] > curr[ch+1]:
                fail = 1
                curr[ch] -= 1
                for j in range(ch+1, len(curr)):
                    curr[j] = 9
                break
        if not fail:
            print("Case #{}: {}".format(i, int(''.join(str(d) for d in curr))))
            break
