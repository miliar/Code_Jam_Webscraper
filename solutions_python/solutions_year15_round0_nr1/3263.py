n = int(raw_input())

max_val = [0 for i in range(n)]
friends = ['' for i in range(n)]

for i in range(n):
    [max_val[i], friends[i]] = raw_input().split()


for i in range(n):
    add = 0
    cur = 0
    index = 0

    while not(index > int(max_val[i])):
        v = int(friends[i][index])
        if index <= cur:
            index += 1
            cur += v
        else:
            add += 1
            cur += 1

    print 'Case #{0}:'.format(i+1), add

