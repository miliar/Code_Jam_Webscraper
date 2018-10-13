import heapq
__author__ = 'Shih-Ting Huang'

"""
2017 Google Code Jam
Author: Shih-Ting Huang
"""


def br_stalls(stall_num, ppl_num):
    stall = [stall_num]
    result_max = 0
    result_min = 0
    for i in range(ppl_num):
        empty = heapq.heappop(stall)
        if empty % 2 is 0:
            empty_stall = [empty//2, empty//2+1]
        else:
            empty_stall = [empty//2+1, empty//2+1]
        result_max, result_min = max(empty_stall), min(empty_stall)
        for x in empty_stall:
            heapq.heappush(stall, x)
    return abs(result_min), abs(result_max)


def main():
    caseNum = int(input())
    with open("Output.txt", "w") as text_file:
        for i in range(1, caseNum+1):
            data = input().split()
            y, z = br_stalls(int(-1 * int(data[0])), int(data[1]))
            print("Case #{}: {} {}".format(i, y, z), file=text_file)


if __name__ == '__main__':
    main()