f = open('B-small-attempt2.in')
fw = open('B-small.out', 'w')

T = int(f.readline())
for t in xrange(T):
    N, R, O, Y, G, B, V = map(int, f.readline().split())
    items = []
    items.append((R, 'R'))
    items.append((Y, 'Y'))
    items.append((B, 'B'))
    items.sort()

    fw.write('Case #' + str(t + 1) + ': ')
    first_diff = items[2][0] - items[1][0]
    second_diff = items[2][0] - items[0][0]
    if first_diff + second_diff > items[2][0]:
        fw.write('IMPOSSIBLE\n')
    else:
        the_rest = items[2][0] - first_diff - second_diff
        ans = (items[2][1] + items[1][1]) * second_diff
        ans += (items[2][1] + items[0][1]) * first_diff
        ans += (items[2][1] + items[1][1] + items[0][1]) * the_rest
        fw.write(ans + '\n')

fw.close()
f.close()
