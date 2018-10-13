import sys

__author__ = 'Oles Savluk'

def solve(D, horses):
    time = 0
    for pos,speed in sorted(horses, reverse=True):
        dist = D - pos
        cur_time = dist / speed
        time = max(cur_time, time)
    return D / time

def toInt(vs):
    return list(map(int, vs))

if __name__ == '__main__':
    lines = sys.stdin.readlines()

    T = int(lines[0].strip())
    it = 1
    for i in range(T):
        D, N = toInt(lines[it].strip().split(' '))
        it += 1
        horses = [toInt(lines[it + h].strip().split(' ')) for h in range(N)]
        it += N
        print('Case #{}: {:.6f}'.format(i + 1, solve(D, horses)))

