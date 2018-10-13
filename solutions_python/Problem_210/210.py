import sys

T = int(sys.stdin.readline().strip())



for t in range(T):
    AC, AJ = [int(i) for i in sys.stdin.readline().split()]

    C_time = 0
    J_time = 0

    activities = []
    for c in range(AC):
        start, end = [int(i) for i in sys.stdin.readline().split()]
        activities.append((start, end, "C"))
        C_time += end-start

    for j in range(AJ):
        start, end = [int(i) for i in sys.stdin.readline().split()]
        activities.append((start, end, "J"))
        J_time += end-start

    activities.sort()

    answer = 0

    C_extra_blocks = []
    J_extra_blocks = []

    for i in range(len(activities)):
        start1, end1, person1 = activities[i-1]
        start2, end2, person2 = activities[i]

        if person1 == "C" and person2 == "C":
            block = (start2-end1 + 1440) % 1440
            if block > 0:
                C_time += block
                C_extra_blocks.append(block)

        elif person1 == "J" and person2 == "J":
            block = (start2-end1 + 1440) % 1440
            if block > 0:
                J_time += block
                J_extra_blocks.append(block)
        else:
            answer += 1

    if C_time > 720:
        # J needs to steal time from C
        C_extra_blocks.sort()
        C_extra_blocks.reverse()

        for block in C_extra_blocks:
            C_time -= block
            answer += 2

            if C_time <= 720:
                break

    elif J_time > 720:
        # C needs to steal time from J
        J_extra_blocks.sort()
        J_extra_blocks.reverse()

        for block in J_extra_blocks:
            J_time -= block
            answer += 2

            if J_time <= 720:
                break

    print("Case #{}: {}".format(t+1, answer))

