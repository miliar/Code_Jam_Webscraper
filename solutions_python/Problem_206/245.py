def solve(D, N, speeds, poses):
    slowest = -1
    for i in range(N):
        t = (D - poses[i]) / speeds[i]
        if t > slowest:
            slowest = t
    return D / slowest

def main():
    T = input()
    for i in xrange(1, T + 1):
        D, N = map(int, raw_input().strip().split())
        speeds = []
        poses = []
        for j in range(N):
            pos, speed = map(int, raw_input().strip().split())
            speeds.append(float(speed))
            poses.append(pos)
        print 'Case #{0}: {1}'.format(i, solve(D, N, speeds, poses))

if __name__ == '__main__':
    main()
