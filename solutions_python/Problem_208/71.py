#!/usr/bin/env python

from queue import PriorityQueue

class Horse():
    def __init__(self, endurance, speed, city):
        self.endurance = endurance
        self.speed = speed
        self.city = city

    def __lt__(self, other):
        return self.endurance > other.endurance or self.speed > other.speed

def nextline():
    return (lambda l: l[0] if len(l) == 1 else l)([int(s) for s in input().split(' ')])

t = nextline()
for case in range(1, t+1):
    n, q = nextline()
    horses = [Horse(*nextline(), i) for i in range(n)]
    adj = [nextline() for _ in range(n)]
    print(f'Case #{case}:', end='')
    for _ in range(q):
        start, destination = [i-1 for i in nextline()]
        horses_used = [[] for _ in range(n)]

        queue = PriorityQueue()
        queue.put((0, horses[start], start))
        while not queue.empty():
            curr_time, curr_horse, curr_node = queue.get()
            # print(curr_time, curr_node)
            if curr_node == destination:
                break
            cand_horses = [h for h in (curr_horse, horses[curr_node]) if h not in horses_used[curr_node]]
            if not cand_horses:
                continue
            if len(cand_horses) == 2:
                if cand_horses[1].endurance >= cand_horses[0].endurance and cand_horses[1].speed >= cand_horses[0].speed:
                    cand_horses.pop(0)
                elif cand_horses[0].endurance >= cand_horses[1].endurance and cand_horses[0].speed >= cand_horses[1].speed:
                    cand_horses.pop(1)
            horses_used[curr_node] += cand_horses
            for city, dist in enumerate(adj[curr_node]):
                if dist == -1:
                    continue
                for horse in cand_horses:
                    if horse.endurance >= dist:
                        queue.put((curr_time + dist/horse.speed, Horse(horse.endurance - dist, horse.speed, horse.city), city))
        else:
            raise Exception()

        print(' ' + str(curr_time), end='')
    print()
