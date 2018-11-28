def compute_mins(lawn):
    def find_min(m, cur):
        (min, positions, curpos) = m
        if cur < min:
            return (cur, [curpos], curpos+1)
        elif cur == min:
            return (cur, [curpos]+positions, curpos+1)
        else:
            return (min, positions, curpos+1)
    return map(lambda x: reduce(find_min, x, (101, [], 0))[0:2], lawn)

def is_mowed_to(lawn, n, m, x, size):
    for y in xrange(n):
        if lawn[y][x] > size:
            return False
    return True

def lawnmower(lawn, n, m):
    mins = compute_mins(lawn)

    for y in xrange(n):
        (min, positions) = mins[y]
        for x in xrange(m):
            if lawn[y][x] > min:
                # the perpendicalur of the min should be mowed, check this
                for pos in positions:
                    if not is_mowed_to(lawn, n, m, pos, min):
                        return False
    return True

if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        [n, m] = [int(_) for _ in raw_input().split()]
        lawn = [[int(_) for _ in raw_input().split()] for y in xrange(n)]
        print('Case #{}: {}'.format(i+1, (lawnmower(lawn, n, m) and 'YES') or 'NO'))
                
