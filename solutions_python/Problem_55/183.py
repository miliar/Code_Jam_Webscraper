from collections import deque

for case in range(int(input())):
    R, k, N = [ int(i) for i in input().split() ]

    line = deque()
    for i in input().split():
        line.appendleft(int(i))

    coaster = deque()
    money = 0
    for i in range(R):
        pop = 0
        group = line.pop()
        while pop + group <= k:
            pop += group
            coaster.appendleft(group)
            money += group
            if len(line) == 0:
                group = 0
                break

            group = line.pop()

        if group != 0:
            line.append(group)
        
        while len(coaster) > 0:
            line.appendleft(coaster.pop())

    print("Case #" + str(case+1) + ": " + str(money))
