"""
Steed 2: Cruise Control
"""


def solve(D, horses):
    maxTime = 0
    for pos, speed in horses:
        t = (D - pos) / speed
        maxTime = max(maxTime, t)
    ans = D / maxTime
    return ans

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1, T + 1):
        D, N = f.readline().strip().split()
        horses = []
        for line in range(int(N)):
            pos, speed = f.readline().strip().split()
            horses.append((int(pos), int(speed)))
        solution = solve(int(D), horses)
        print("Case #{0}: {1:.6f}".format(case, solution))
