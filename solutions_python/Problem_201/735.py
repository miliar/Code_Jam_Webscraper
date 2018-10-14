def find(start, goal, l):
    i = 0
    for val, _ in l[start:]:
        if val == goal:
            return start + i
        i += 1
    l.append((goal, 0))
    return len(l) - 1

def solve():
    N, K = map(int, raw_input().split())
    seg = [(N, 1)] # size, count
    pos = 0
    while K > 0:
        #split and update
        size, count = seg[pos]
        K -= count
        if size % 2 == 1:
            new_size = (size-1)/2
            pos2 = find(pos + 1, new_size, seg)

            seg[pos2] = (seg[pos2][0], seg[pos2][1]+2*count)
        else:
            new_size = size / 2
            new_size2 = (size-1) / 2

            #find new_size
            pos2 = find(pos + 1, new_size, seg)
            pos3 = find(pos + 1, new_size2, seg)

            seg[pos2] = (seg[pos2][0], seg[pos2][1]+count)
            seg[pos3] = (seg[pos3][0], seg[pos3][1]+count)

        pos += 1
    size, _ = seg[pos-1]
    return "{} {}".format(size/2, (size-1)/2)

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(1, T+1):
        print "Case #{}: {}".format(i, solve())
