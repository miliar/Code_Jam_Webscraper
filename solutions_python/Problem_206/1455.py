import sys

def solve(dest, horses):
    time = 0
    for k, s in horses:
        reach = (dest-k)/(s*1.0)
        if reach > time:
            time = reach
    return dest/time

def read_ints():
    return map(lambda x: int(x.strip()), raw_input().split())


def main():
    T = int(raw_input())
    for i in xrange(1, T+1):
        dest, n = read_ints()
        horses = []
        for j in xrange(n):
            horses.append(read_ints())
        print('Case #{0}: {1:.6f}'.format(i, solve(dest,horses)))

main()
