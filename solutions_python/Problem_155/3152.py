f = open('a.in', 'r')
T = 0
t = 0

for line in f:
    if T == 0:
        T = int(line)
        continue

    t += 1
    s_max, n = line.split(' ')
    s_max = int(s_max)
    n = [ int(x) for x in n.strip() ]

    result = [0]
    for i in range(s_max, -1, -1):
        # print(n[:i - len(n)], i)
        result.append(i - sum(n[:i - len(n)])) # = max(result, i - sum(n[:i - len(n)]))

    print('Case #{0}: {1}'.format(t, max(result)))
    # print(result)
