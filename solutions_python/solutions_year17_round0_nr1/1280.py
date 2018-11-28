__author__ = 'Shih-Ting Huang'

"""
2017 Google Code Jam
Author: Shih-Ting Huang
"""


def pancake(pancakes, k_size):
    size = len(pancakes)
    flip_count = 0
    for i in range(size - k_size + 1):
        if pancakes[i] is '-':
            flip_count += 1
            for j in range(k_size):
                if pancakes[i+j] is '-':
                    pancakes[i+j] = '+'
                else:
                    pancakes[i+j] = '-'
        else:
            pass
        if pancakes[size-1 - i] is '-':
            flip_count += 1
            for j in range(k_size):
                if pancakes[size-1 - i - j] is '-':
                    pancakes[size-1 - i - j] = '+'
                else:
                    pancakes[size - 1 - i - j] = '-'
        else:
            pass
    result = flip_count
    for x in pancakes:
        if x is '-':
            result = 'IMPOSSIBLE'
    return result


def main():
    caseNum = int(input())
    with open("Output.txt", "w") as text_file:
        for i in range(1, caseNum+1):
            case = input().split()
            result = pancake(list(case[0]), int(case[1]))
            print("Case #{}: {}".format(i, result), file=text_file)


if __name__ == '__main__':
    main()