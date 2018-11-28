#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# vi: set fileencoding=utf-8 :

class PriorityQueue:

    def __init__(self, priority):
        self.heap_list = [[]]
        self.priority = priority
        return


    def pop(self):
        if self.size() <= 0:
            return []
        if self.size() == 1:
            return self.heap_list.pop()
        else:
            first = self.heap_list[1]
            self.heap_list[1] = self.heap_list.pop()
            self.shift_down(1)
            return first


    def push(self, element):
        self.heap_list.append(element)
        self.shift_up(self.size())
        return


    def shift_down(self, i):
        if i * 2 >= len(self.heap_list):
            return
        if i * 2 == self.size() or self.priority(self.heap_list[2 * i], self.heap_list[2 * i + 1]) >= 0:
            prior_child_index = 2 * i
        else:
            prior_child_index = 2 * i + 1
        if self.priority(self.heap_list[i], self.heap_list[prior_child_index]) < 0:
            self.swap(i, prior_child_index)
            self.shift_down(prior_child_index)
        return


    def shift_up(self, i):
        if i <= 1:
            return
        if self.priority(self.heap_list[i // 2], self.heap_list[i]) < 0:
            self.swap(i // 2, i)
            self.shift_up(i // 2)
        return


    def size(self):
        return len(self.heap_list) - 1


    def swap(self, i, j):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]
        return

def pri(interval1, interval2):
    if interval1[1] - interval1[0] != interval2[1] - interval2[0]:
        return (interval1[1] - interval1[0]) - (interval2[1] - interval2[0])
    return interval2[0] - interval1[0]


def solve(N, K):
    stalls = PriorityQueue(pri)
    stalls.push([0, N - 1])
    for k in range(K):
        free_stall = stalls.pop()
        center = (free_stall[0] + free_stall[1]) // 2
        L_s = center - free_stall[0]
        if L_s > 0:
            stalls.push([free_stall[0], center - 1])
        R_s = free_stall[1] - center
        if R_s > 0:
            stalls.push([center + 1, free_stall[1]])
    return '%d %d' % (R_s, L_s)


T = int(input())
for case_number in range(1, T + 1):
    N, K = map(int, input().split())
    print('Case #%d: %s' % (case_number, solve(N, K)))
