#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from itertools import combinations

class Rank():
    def run(self, n):
        all_combinations = [(n,),]
        set = range(2, n)
        for r in range(1, len(set) + 1):
            for c in combinations(set, r):
                all_combinations.append(c + (n,))

        pure_combinations = []
        print len(all_combinations)

        for i in all_combinations:
            if self.__is_pure_combination(i):
                pure_combinations.append(i)

        # print pure_combinations

        return len(pure_combinations)

    def __is_pure_combination(self, list):
        number = list[-1]

        return self.__is_in_set(number, list)
        
    def __is_in_set(self, number, list):
        number_rank = list.index(number) + 1
        if number_rank == 1:
            return True

        if number_rank in list:
            return self.__is_in_set(number_rank, list)

        return False

    def dict(self, n):
        dict = {2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 14, 
                8: 24, 9: 43, 10: 77, 11: 140, 12: 256, 
                13: 472, 14: 874, 15: 1628, 16: 3045, 
                17: 5719, 18: 10780, 19: 20388, 20: 38674, 
                21: 73562, 22: 140268, 23: 268066, 24: 513350, 25: 984911}

        return dict[n]

if __name__ == "__main__":
    rank = Rank()
    results = []
    result_dict = {}

    with open("C-small-attempt1.in.txt") as in_file:
        t = int(in_file.readline())
        for i in range(t):
            n = int(in_file.readline())
            result = rank.dict(n) % 100003
            result_dict[n] = result
            results.append(result)
        print "results", result_dict

    with open("ouput.txt", "w") as out_file:
        for i in range(len(results)):
            line = "Case #%s: %s\n" % (i + 1, results[i])
            out_file.write(line)