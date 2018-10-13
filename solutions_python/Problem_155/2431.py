




def solve(n, s):
    add = 0
    total = 0

    for i, count in enumerate(s):
        if count <= 0:
            continue
        if total < i:
            add += i - total
            total += i - total
        total += count
    return add

def main():
    with open('A.in', 'r') as f:
        with open('A.out', 'w') as g:
            lines = f.readlines()
            n = int(lines[0])
            i = 1
            for line in lines[1:]:
                n, data = line.strip().split(' ')
                g.write('Case #%d: %d\n' % (i, solve(int(n), map(int, data))))
                i += 1


if __name__ == '__main__':
    main()