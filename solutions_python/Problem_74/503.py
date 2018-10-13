# Google Code Jam 2011 qualifying round.
# Fill individual queues of buttons for O and B, and common queue to
# synchronize.  Process queues.
# Example input: O 2 B 1 B 2 O 4
# O queue: 2 4
# B queue: 1 2
# Simulation:
#     pos    CommonQueue  queue     press
#     O B                 O    B    O  B
#  0: 1 1    O2 B1 B2 O4  2 4  1 2
#  1: 2 1
#  2: 2 1    B1 B2 O4     4         2
#  3: 3 1    B2 O4             2       1
#  4: 4 2
#  5: 4 2    O4                -       2
#  6: 4 2    -            -         4

from collections import deque   # Faster to delete at front
import sys
def doCase(queue, botqueue):
    time = 0
    pos = {}
    pos['O'] = pos['B'] = 1
    while len(queue) > 0:
        time += 1
        pressing = ''
        (bot, button) = queue[0]
        if pos[bot] == button:  # We're there, press
            queue.popleft()
            botqueue[bot].popleft()
            pressing = bot
        for bot in ('O', 'B'):
            if pressing != bot and botqueue[bot]:
                if botqueue[bot][0] > pos[bot]:
                    pos[bot] += 1
                if  botqueue[bot][0] < pos[bot]:
                    pos[bot] -= 1
    return time

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        goal = file.readline().split()[1:]
        queue = zip(goal[0::2], goal[1::2])
        queue = [(bot,int(button)) for (bot,button) in queue]
        botqueue = {}
        for bot in ('O', 'B'):
            botqueue[bot] = deque([int(y) for (x,y) in queue if x == bot])
        answer = doCase(deque(queue), botqueue)
        print 'Case #{0}: {1}'.format(case, answer)
run()
