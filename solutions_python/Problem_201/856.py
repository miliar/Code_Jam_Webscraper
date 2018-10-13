#!/usr/bin/python3

import sys
from heapq import *

max_heap_size = 0

def smarter_bathroom_simulation(stalls, people):
    def add_space(heap, heapvals, numstalls):
        global max_heap_size

        if numstalls in heapvals:
            heapvals[numstalls] += 1
        else:
            heapvals[numstalls] = 1
            heappush(heap, -numstalls)
        max_heap_size = max(max_heap_size, len(heap))
    def fetch_space(heap, heapvals):
        numstalls = -heap[0]
        heapvals[numstalls] -= 1
        if heapvals[numstalls] < 1:
            del heapvals[numstalls]
            heappop(heap)
        return numstalls

    heapvals = {stalls: 1}
    heap = [-stalls]
    min_space = -1
    max_space = -1
    for i in range(0, people):
        numstalls = fetch_space(heap, heapvals)
        min_space = (numstalls - 1) // 2
        max_space = numstalls // 2
        add_space(heap, heapvals, min_space)
        add_space(heap, heapvals, max_space)
    return (min_space, max_space)

def stupid_bathroom_simulation(stalls, people):
    unoccupied = object()
    occupied = object()

    def occupy_stall(stall_state):
        ext_min = -1
        ext_max = -1
        ext_idx = -1
        for (idx, extent) in enumerate(stall_state):
            if extent[0] is unoccupied:
                cur_min = (extent[1] - 1) // 2
                cur_max = extent[1] // 2
                if (cur_min, cur_max) > (ext_min, ext_max):
                    ext_min, ext_max = cur_min, cur_max
                    ext_idx = idx
        if ext_idx == -1:
            raise RuntimeError("Bathroom must be full!")
        assert ext_min >= 0
        assert ext_min <= ext_max
        assert stall_state[ext_idx][0] is unoccupied
        assert stall_state[ext_idx][1] == (ext_min + ext_max + 1)
        new_extents = []
        if ext_min < 1:
            assert stall_state[ext_idx][1] < 3
            assert ext_max < 2
            if ext_max > 0:
                new_extents = [(occupied, 1), (unoccupied, ext_max)]
            else:
                assert stall_state[ext_idx][1] < 2
                new_extents = [(occupied, 1)]
        else:
            new_extents = [(unoccupied, ext_min),
                           (occupied, 1),
                           (unoccupied, ext_max)]
        stall_state[ext_idx:ext_idx + 1] = new_extents
        chg_start = min(ext_idx - 1, 0)
        chg_end = min(ext_idx + len(new_extents) + 1, len(stall_state))
        new_extents = stall_state[chg_start:chg_end]
        idx = 0
        while (idx + 1) < len(new_extents):
            if new_extents[idx][0] is new_extents[idx + 1][0]:
                sum_ppl = new_extents[idx][1] + new_extents[idx + 1][1]
                new_extents[idx:idx + 2] = [(new_extents[idx][0], sum_ppl)]
            else:
                idx = idx + 1
        stall_state[chg_start:chg_end] = new_extents
        return (ext_min, ext_max)

    def stall_state_as_string(stall_state):
        def ext_iter(stall_state):
            yield 'O'
            for extent in stall_state:
                yield ('O' if extent[0] is occupied else '-') * extent[1]
            yield 'O'
        return ''.join(ext_iter(stall_state))

    stall_state = [(unoccupied, stalls)]
    for i in range(0, people):
        mindist, maxdist = occupy_stall(stall_state)
        my_dist = (mindist, maxdist)
        smart_dist = smarter_bathroom_simulation(stalls, i + 1)
        assert my_dist == smart_dist
        print("{!r:<8} {}".format(my_dist, stall_state_as_string(stall_state)))

def process_stdin():
    numnums = int(sys.stdin.readline())
    for case in range(1, numnums + 1):
        stalls, people = [int(x) for x in sys.stdin.readline().split()]
        min_stalls, max_stalls = smarter_bathroom_simulation(stalls, people)
        print("Case #{}: {} {}".format(case, max_stalls, min_stalls))

if __name__ == '__main__':
    process_stdin()
