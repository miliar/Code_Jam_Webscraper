#!/usr/bin/env python3
import heapq

class ConsecStalls:
    StallCounter = 0
    def __init__(self, length, num):
        self.length = length
        self.num = num
        self.unique = ConsecStalls.StallCounter
        ConsecStalls.StallCounter += 1

    def create_heap_element(self):
        return (-1 * self.length, self.unique, self)

class Instance:
    def __init__(self, name, N, K):
        self.name = name
        initial_stalls = ConsecStalls(N, 1)
        self.heap = [initial_stalls.create_heap_element()]
        heapq.heapify(self.heap)
        self.remaining = K
        self.maxLs = None
        self.minLs = None
        self.final_broken_block = None

    def solve(self):
        enough_breaking_up = False
        while not enough_breaking_up:
            enough_breaking_up = self.work_through_heap()
        self.last_placement_found()

    def work_through_heap(self):
        #print('\nREMAINING:', self.remaining)
        #self.dump_heap()
        maximum = self.get_largest_element()

        enough_breaking_up = True
        if not self.all_get_assigned(maximum):
            self.remaining -= maximum.num
            if self.remaining < 0:
                raise ValueError('Too many assigned')
            elif self.remaining > 0:
                new_elements = self.split_maximum(maximum)
                self.push_stalls_to_heap(new_elements)
                enough_breaking_up = False
        if enough_breaking_up:
            self.final_broken_block = maximum
        return enough_breaking_up

    def dump_heap(self):
        print('DUMPING HEAP / LENGTH: ', len(self.heap))
        for idx, uniq, val in self.heap:
            print((val.length, val.num))

    def get_largest_element(self):
        if not self.heap:
            raise ValueError('Expected K < N')
        maximum = self.aggregate_maximal_values()
        return maximum

    def aggregate_maximal_values(self):
        maximum = self.pop_from_heap()
        while self.heap:
            candidate_maximum = self.pop_from_heap()
            if maximum.length == candidate_maximum.length:
                maximum.num += candidate_maximum.num
            else:
                self.single_safe_push(candidate_maximum)
                break
        return maximum

    def pop_from_heap(self):
        return heapq.heappop(self.heap)[2]

    def all_get_assigned(self, maximum):
        return maximum.num > self.remaining

    def split_maximum(self, maximum):
        maxlength = maximum.length
        if maxlength == 1:
            new_elements = []
        elif maxlength == 2:
            new_elements = [ConsecStalls(1, maximum.num)]
        elif (maxlength - 1) % 2 == 0:
            new_elements = [ConsecStalls((maxlength - 1) // 2, maximum.num * 2)]
        else:
            new_elements = [ConsecStalls((maxlength - 1)// 2, maximum.num),
                            ConsecStalls((maxlength - 1) // 2 + 1, maximum.num)]

        return new_elements

    def push_stalls_to_heap(self, new_elements):
        for element in new_elements:
            self.single_safe_push(element)

    def single_safe_push(self, element):
        heap_element = element.create_heap_element()
        heapq.heappush(self.heap, heap_element)

    def last_placement_found(self):
        maxlen = self.final_broken_block.length
        #print('Optimum: ', maxlen)

        minLs = (maxlen - 1)// 2
        if (maxlen - 1) % 2 != 0:
            maxLs = minLs + 1
        else:
            maxLs = minLs

        self.minLs = minLs
        self.maxLs = maxLs

    def print_optimum(self):
        print_case(self.name, self.maxLs, self.minLs)

def print_case(name, maxLs, minLs):
    string = 'Case #' + str(name) + ': ' + str(maxLs) + ' ' + str(minLs)
    print(string)

def main():
    testcases = int(input())
    for i in range(testcases):
        intstr = input().strip().split()
        N, K = [int(x) for x in intstr]
        if N == K:
            print_case(i + 1, 0, 0)
        else:
            instance = Instance(i + 1, N, K)
            instance.solve()
            instance.print_optimum()

if __name__ == '__main__':
    main()
