t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    result = []
    given = []
    for j in range(r):
        given.append(input())
        result.append([])

    not_blank_idx = []
    for j in range(r):
        chars = []
        for ch in given[j]:
            if ch != '?':
                chars.append(ch)
        if len(chars) > 0:
            not_blank_idx.append(j)
            idx = 0
            for ch in given[j]:
                result[j].append(chars[idx])
                if ch != '?':
                    if idx < len(chars) - 1:
                        idx += 1
        elif len(not_blank_idx) > 0:
            for ch in result[not_blank_idx[-1]]:
                result[j].append(ch)

    for j in range(not_blank_idx[0]):
        for ch in result[not_blank_idx[0]]:
            result[j].append(ch)
    print('Case #%d:' % (i + 1))
    for row in result:
        print(''.join(row))
