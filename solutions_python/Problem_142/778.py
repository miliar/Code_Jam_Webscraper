import sys

def count(line):
    symbol = line[0]
    counts = []
    compact = symbol
    count = 0
    for i in range(len(line)):
        if symbol == line[i]:
            count += 1
        else:
            counts.append(count)
            symbol = line[i]
            compact += symbol
            count = 1
    counts.append(count)
    return (compact, counts)

lines = sys.stdin.readlines()
T = int(lines[0])
line_id = 0
for t in range(1, T + 1):
    line_id += 1
    N = int(lines[line_id])
    counts = []
    for n in range(N):
        line_id += 1
        counts.append(count(lines[line_id].strip()))
    canonical = counts[0][0]
    can_win = True
    for cnt in counts:
        if cnt[0] != canonical:
            print('Case #{}: Fegla Won'.format(t))
            can_win = False
            break
    if can_win:
        moves = 0
        for i in range(len(canonical)):
            s = 0
            for cnt in counts:
                s += cnt[1][i]
            avg = round(s / N)
            for cnt in counts:
                moves += abs(cnt[1][i] - avg)
        print('Case #{}: {}'.format(t, moves))

