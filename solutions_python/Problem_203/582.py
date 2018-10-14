import math

n = int(raw_input())

for i in range(1, n + 1):
    R, C = [int(x) for x in raw_input().split(' ')]

    arr = []
    for j in range(1, R + 1):
        arr.append(raw_input())

    charmap = {'?' : []}
    for j in range(0, R):
        for k in range(0, len(arr[j])):
            c = arr[j][k]
            if c in charmap:
                charmap[c].append((j, k))
            else:
                charmap[c] = [(j, k)]

    for k in charmap.keys():
        if k == '?':
            continue
        l = charmap[k]
        if len(l) == 0 or len(l) == 1:
            continue

        for x in l:
            for y in l:
                for z in range(min(x[0], y[0]), max(x[0], y[0]) + 1):
                    for a in range(min(x[1], y[1]), max(x[1], y[1]) + 1):
                        tmp = list(arr[z])
                        tmp[a] = k
                        arr[z] = ''.join(tmp)

    for x in range(0, len(arr)):
        for y in range(0, len(arr[x])):
            if arr[x][y] == '?':
                pre = arr[x][:y].replace('?', '')
                post = arr[x][y+1:].replace('?', '')
                if len(pre) > 0:
                    tmp = list(arr[x])
                    tmp[y] = pre[-1]
                    arr[x] = ''.join(tmp)
                elif len(post) > 0:
                    tmp = list(arr[x])
                    tmp[y] = post[0]
                    arr[x] = ''.join(tmp)

    for x in range(0, len(arr)):
        for y in range(0, len(arr[x])):
            if arr[x][y] == '?':
                sl = []
                for z in range(0, R):
                    sl.append(arr[z][y])
                sl = ''.join(sl)
                pre = sl[:x].replace('?', '')
                post = sl[x+1:].replace('?', '')
                if len(pre) > 0:
                    tmp = list(arr[x])
                    tmp[y] = pre[-1]
                    arr[x] = ''.join(tmp)
                elif len(post) > 0:
                    tmp = list(arr[x])
                    tmp[y] = post[0]
                    arr[x] = ''.join(tmp)


    print("Case #{}:".format(i))

    for j in range(0, R):
        print(arr[j])
