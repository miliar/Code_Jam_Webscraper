import heapq

def multi_max(lst):
    max_val = None
    for index, val in enumerate(lst):
        if max_val is None or (val != -1 and val > max_val):
            indices = [index]
            max_val = val
        elif val == max_val:
            indices.append(index)
    return indices


def multi_min(lst):
    min_val = None
    for index, val in enumerate(lst):
        if min_val is None or (val != -1 and val < min_val):
            indices = [index]
            min_val = val
        elif val == min_val:
            indices.append(index)
    return indices


class Bathroom():
    def __init__(self, num_stalls):
        self.intervals = [(num_stalls * -1, 0, num_stalls + 1)]

    def next_pos(self):
        dist, l_idx, r_idx = self.intervals[0]
        midpoint = l_idx + int((r_idx - l_idx) / 2)
        return (midpoint, l_idx, r_idx)

    def add_person(self):
        midpoint, l_idx, r_idx = self.next_pos()
        heapq.heappushpop(
            self.intervals, ((midpoint - 1 - l_idx) * -1, l_idx, midpoint))
        heapq.heappush(
            self.intervals, ((r_idx - midpoint - 1) * -1, midpoint, r_idx))


def main():
    num_cases = int(input())
    for case in range(num_cases):
        params = input().split(' ')
        num_stalls = int(params[0])
        num_people = int(params[1])

        b = Bathroom(num_stalls)
        for n in range(num_people - 1):
            b.add_person()

        midpoint, l_idx, r_idx = b.next_pos()
        ls = r_idx - midpoint - 1
        rs = midpoint - 1 - l_idx

        print('Case #{0}: {1} {2}'.format(case + 1, max(ls, rs), min(ls, rs)))


main()
