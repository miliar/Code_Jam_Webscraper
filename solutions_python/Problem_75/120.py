N = int(input())

for num in range(1, N + 1):
    inp = input().split()
    combine = {}
    opposed = set()
    i = int(inp[0])
    for j in range(1, 1 + i):
        combine[inp[j][:2]] = inp[j][2]
        combine[inp[j][1::-1]] = inp[j][2]
    i = i + 1
    for j in range(i + 1, i + 1 + int(inp[i])):
        opposed.add(inp[j])
        opposed.add(inp[j][::-1])
    ans = ['@']
    for elem in inp[-1]:
        if ans[-1] + elem in combine:
            ans[-1] = combine[ans[-1] + elem]
        else:
            for elem1 in ans:
                if elem1 + elem in opposed:
                    ans = ['@']
                    break
            else:
                ans.append(elem)
    ans = ', '.join(ans[1:])
    print("Case #", num, ": [", ans, "]", sep = '')

