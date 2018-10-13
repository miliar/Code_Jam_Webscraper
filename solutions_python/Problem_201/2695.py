#!/usr/bin/env pypy
from __future__ import print_function

import sys
from collections import OrderedDict, namedtuple
from pprint import pprint


def _add_to_dict_list(dict, key, item):
    if key in dict:
        dict[key].append(item)
    else:
        dict[key] = [item]

Range = namedtuple('Range', ('start', 'end'))


class Case(object):

    def __init__(self, idx, stalls, people):
        self.idx = int(idx)
        self.stalls = int(stalls) + 1

        self.stall_used_map = OrderedDict()
        self.stall_used_map[0] = True
        self.stall_used_map[self.stalls] = True

        self.empty_stall_ranges = OrderedDict()
        self.init_empty_ranges()

        self.people = int(people)

    def __str__(self):
        return "Case #%i: %i %i" % (self.idx, 0, 0)

    def show_map(self):
        for i in range(0, self.stalls + 1):
            if self.stall_used_map.get(i, False):
                print('o', end='', file=sys.stderr)
            else:
                print('.', end='', file=sys.stderr)
        print('')

    def init_empty_ranges(self):
        self.empty_stall_ranges = OrderedDict()
        start = 1
        end = self.stalls - 1
        self.empty_stall_ranges[end-start] = [Range(start, end)]
        return

    def refresh_empty_stall_ranges(self, idx_used):
        new_stall_ranges = OrderedDict()
        for leng, range_list in self.empty_stall_ranges.items():
            for rang in range_list:
                if rang.start <= idx_used <= rang.end:
                    # 3 possibilities:
                    # start 3, end 3
                    if rang.start == rang.end:
                        continue
                    # start 3, end 4
                    if rang.start + 1 == rang.end:
                        if idx_used == rang.start:
                            _add_to_dict_list(new_stall_ranges, 1, Range(rang.end, rang.end))
                        else:
                            _add_to_dict_list(new_stall_ranges, 1, Range(rang.start, rang.start))
                    # start 7, end 10
                    else:
                        if idx_used == rang.start:
                            _add_to_dict_list(new_stall_ranges, rang.end - rang.start - 1,
                                              Range(rang.start + 1, rang.end))
                        elif idx_used == rang.end:
                            _add_to_dict_list(new_stall_ranges, rang.end - rang.start - 1,
                                              Range(rang.start, rang.end - 1))
                        else:
                            first_range_end = idx_used - 1
                            _add_to_dict_list(new_stall_ranges, first_range_end - rang.start,
                                              Range(rang.start, first_range_end))
                            second_range_start = idx_used + 1
                            _add_to_dict_list(new_stall_ranges, rang.end - second_range_start,
                                              Range(second_range_start, rang.end))
                else:
                    _add_to_dict_list(new_stall_ranges, leng, rang)

        self.empty_stall_ranges = OrderedDict(sorted(new_stall_ranges.items(), reverse=True))
        # self.empty_stall_ranges = new_stall_ranges
        return new_stall_ranges

    def get_ls_rs_for_empty_stall(self, empty_stall_idx):
        for leng, range_list in self.empty_stall_ranges.items():
            for rang in range_list:
                if rang.start <= empty_stall_idx <= rang.end:
                    return empty_stall_idx - rang.start, rang.end - empty_stall_idx
        return 0, 0

    def get_min_max_for_empty_stall(self, empty_stall_idx):
        ls, rs = self.get_ls_rs_for_empty_stall(empty_stall_idx)
        return min([ls, rs]), max([ls, rs])

    def choose_next_stall(self):
        best_min = dict()
        mininmax_cache = dict()
        # No more free stalls...
        if len(self.empty_stall_ranges) == 0:
            return None, 0, 0

        long, range_list = next(iter(self.empty_stall_ranges.items()))
        # for leng, range_list in self.empty_stall_ranges.items():
        for rang in range_list:
            # start at middle of range
            middle = int((rang.end + rang.start) / 2)
            middle_below = middle - 1
            middle_above = middle + 1
            if rang.start <= middle <= rang.end:
                tmin, tmax = self.get_min_max_for_empty_stall(middle)
                _add_to_dict_list(best_min, tmin, middle)
                mininmax_cache[middle] = tmin, tmax
            if rang.start <= middle_below <= rang.end:
                tmin, tmax = self.get_min_max_for_empty_stall(middle_below)
                _add_to_dict_list(best_min, tmin, middle_below)
                mininmax_cache[middle_below] = tmin, tmax
            if rang.start <= middle_above <= rang.end:
                tmin, tmax = self.get_min_max_for_empty_stall(middle_above)
                _add_to_dict_list(best_min, tmin, middle_above)
                mininmax_cache[middle_above] = tmin, tmax
        best_min_dist = max(best_min)
        win_idx = None
        if len(best_min[best_min_dist]) == 1:
            win_idx = best_min[best_min_dist][0]
        elif len(best_min[best_min_dist]) > 1:
            best_max = dict()
            for s in best_min[best_min_dist]:
                tmin, tmax = mininmax_cache[s]
                _add_to_dict_list(best_max, tmax, s)
            best_max_dist = max(best_max)
            win_idx = best_max[best_max_dist][0]
        if win_idx:
            win_idx_min, win_idx_max = mininmax_cache[win_idx]
            return win_idx, win_idx_max, win_idx_min
        else:
            return None, 0, 0

    def use_stall(self, idx):
        self.stall_used_map[idx] = True
        self.refresh_empty_stall_ranges(idx)

    def print_final_state(self):
        for i in range(0, self.people):
            # print(self.show_map())
            next_stall_id, tmax, tmin = self.choose_next_stall()
            # print("Next stall to choose: ", next_stall_id, " MAX:", tmax, " MIN:", tmin)
            if i + 1 == self.people:
                print("Case #%i: %i %i" % (self.idx, tmax, tmin))
            if next_stall_id:
                self.use_stall(next_stall_id)
            else:
                print("Case #%i: 0 0" % (self.idx))
                break


def read_cases(file):
    cases = []
    with open(file) as f:
        cases_raw = int(f.readline())
        for idx in range(1, cases_raw+1):
            stalls_data_raw = f.readline()
            n, k = stalls_data_raw.split(" ")
            cases.append(Case(idx, n, k))
    return cases


if __name__ == '__main__':
    try:
        cases = read_cases(sys.argv[1])
        for case in cases:
            case.print_final_state()
    except KeyboardInterrupt:
        exit()