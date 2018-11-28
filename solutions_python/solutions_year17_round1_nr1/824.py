t = int(input())
f2 = open('output.txt', 'w', encoding = "utf-8")
for i in range(t):
    n, m = map(int, input().split(' '))
    arr = []
    for j in range(n):
        arr.append(list(input()))
    indices = []
    for k in range(n):
        for l in range(m):
            indices.append([k,l])
    i0 = 0
    while i0 < len(indices):
        k1, k2 = indices[i0][0], indices[i0][1]
        ends = []
        for k in range(k1, n):
            for l in range(k2, m):
                ends.append([k,l])
        ends = sorted(ends, key = lambda end: end[0] + end[1], reverse=True)
        for e in ends:
            let_n = 0
            b = True
            h = ''
            for k in range(k1, e[0]+1):
                for l in range(k2, e[1]+1):
                    if arr[k][l] != '?':
                        let_n += 1
                        if let_n > 1:
                            b = False
                            break
                        h = arr[k][l]
            if b:
                if h != '':
                    for k in range(k1, e[0]+1):
                        for l in range(k2, e[1]+1):
                            arr[k][l] = h
                            try:
                                indices.remove([k, l])
                            except:
                                pass
                    break
    f2.write('Case #{}:\n'.format(i+1))
    for k in arr:
        f2.write(''.join(k)+'\n')
f2.close()