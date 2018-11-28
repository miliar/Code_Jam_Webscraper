import sys

def solve():
    C, J = map(int, sys.stdin.readline().rstrip().split())

    tasks = []

    Ctimes = 0
    for i in range(C):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        Ctimes += end - start
        tasks.append((start, end, 'C'))

    Jtimes = 0
    for i in range(J):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        Jtimes += end - start
        tasks.append((start, end, 'J'))

    tasks = sorted(tasks)

    transitions = 0
    trans_times = 0
    for i in range(C+J):
        prev_task = (i-1)%(C+J)

        if tasks[prev_task][2] != tasks[i][2]:
            transitions += 1
            trans_times += (tasks[i][0] - tasks[prev_task][1]) % (60 * 24)

    # print Ctimes, Jtimes, trans_times
    if min(Ctimes, Jtimes) + trans_times >= 720:
        return transitions

    # Now have to start bothering the parent with more time
    min_time = min(Ctimes, Jtimes)
    x = 'C' if Ctimes > Jtimes else 'J'

    time_needed = 720 - min_time - trans_times

    gaps = []
    for i in range(C+J):
        if tasks[i][2] != x:
            continue

        next_task = (i+1)%(C+J)
        if tasks[next_task][2] == x:
            gaps.append((tasks[next_task][0]-tasks[i][1]) % (60*24))

    gaps = sorted(gaps)[::-1]
    for gap in gaps:
        if time_needed <= 0:
            break

        transitions += 2
        time_needed -= gap

    # assert time_needed <= 0
    return transitions

def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        print 'Case #{}: {}'.format(t, solve())

if __name__ == "__main__":
    main()
