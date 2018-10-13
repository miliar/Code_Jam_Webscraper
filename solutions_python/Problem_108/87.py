
# vines: (distance, length)
def solve(N, D, vines):
    frontier = []
    frontier.append((0, vines[0][0]))
    visited = set(frontier)
    while frontier:
        (v, swing) = frontier[0]
        # print (v, swing)
        del frontier[0]
        if vines[v][0] + swing >= D:
            return 'YES'
        for j in range(v + 1, N):
            # print vines[v][0] + swing, vines[j][0]
            if vines[v][0] + swing >= vines[j][0]:
                nswing = min(vines[j][0] - vines[v][0], vines[j][1])
                if (j, nswing) not in visited:
                    frontier.append((j, nswing))
                    visited.add((j, nswing))
    return 'NO'
        

file = open('A-small-attempt0.in', 'r')
if __name__ == '__main__':
    T = int(file.readline())
    for case in range(1, T+1):
        N = int(file.readline())
        vines = []
        for i in range(N):
            (d, l) = tuple(map(int, file.readline().split()))
            vines.append((d, l))
        D = int(file.readline())
        print 'Case #{}:'.format(case), solve(N, D, vines)
