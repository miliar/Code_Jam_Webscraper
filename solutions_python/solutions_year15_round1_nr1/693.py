f = open('A-large.in', 'r')
outf = open('A-large-out.txt', 'w')

T = int(f.readline())

def first_way(N, mushrooms):
    total = 0
    for i in range(N-1):
        if mushrooms[i] > mushrooms[i+1]:
            total += mushrooms[i] - mushrooms[i+1]
    return total

def second_way(N, mushrooms):
    max_gap = 0
    for i in range(N-1):
        max_gap = max(max_gap, mushrooms[i] - mushrooms[i+1])
    total = 0
    for i in range(N-1):
        if mushrooms[i] < max_gap:
            total += mushrooms[i]
        else:
            total += max_gap
    return total


for test_ind in range(T):
    N = int(f.readline())
    mushrooms = map(int, f.readline().split())
    out_str = 'Case #' + str(test_ind + 1) + ': ' + str(first_way(N, mushrooms)) + ' ' + str(second_way(N, mushrooms)) + '\n'
    outf.write(out_str)

f.close()
outf.close()
