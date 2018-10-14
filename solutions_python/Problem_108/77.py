def solve(d, l, N, D):
    track_index = 2
    to_inv = [(1, 0, d[1])]
    while to_inv:
        now_inv = to_inv.pop(0)
        start = now_inv[1]
        index = now_inv[0]
        length = l[index]
        reach = start + 2 * now_inv[2]
        if reach >= D:
            return True
        while (track_index <= N) and (start <= d[track_index] <= reach):
            if l[track_index] < d[track_index] - d[index]:
                to_inv.append((track_index, d[track_index] - l[track_index], l[track_index]))
            else:
                to_inv.append((track_index, d[index], d[track_index] - d[index]))
            track_index += 1
    return False

if __name__ == '__main__':
    #f = open('sample.in')
    #output = open('sample.out', 'w')
    f = open('A-large.in')
    output = open('A-large.out', 'w')
    test_case = int(f.readline())
    for i in range(test_case):
        N = int(f.readline())
        d = {}
        l = {}
        for j in range(1, N+1):
            line = f.readline()
            line = line.split()
            d[j] = int(line[0])
            l[j] = int(line[1])
        D = int(f.readline())
        yes_or_no = solve(d, l, N, D)
        if yes_or_no:
            output.write('Case #{}: YES\n'.format(i+1))
        else:
            output.write('Case #{}: NO\n'.format(i+1))
    f.close()
    output.close()