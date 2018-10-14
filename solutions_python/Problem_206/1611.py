import fileinput



def solve(V, E, edges):
    return V, E, len(edges)  # count edges

f = fileinput.input()
#f = open("input")


T = int(f.readline())
for case in range(1, T + 1):
    D, N = [int(x) for x in f.readline().split()]
    horses = []
    vel = float('inf')
    for horse in range(N):
        ki, si = [int(x) for x in f.readline().split()]
        vel = min(si/float(D-ki), vel)

    print("Case #{0}: {1}".format(case, vel*D))

