#(c) 2017 Tuan Tran

import sys

def flip_k_cakes(pancakes_list, start, k):
    for i in range(start, start + k):
        pancakes_list[i] = not pancakes_list[i]

def min_flip(pancakes_list, k):
    count = 0
    for i in range(len(pancakes_list) - k + 1):
        if not pancakes_list[i]:
            flip_k_cakes(pancakes_list, i, k)
            count += 1
    for i in range(len(pancakes_list) - k + 1, len(pancakes_list)):
        if not pancakes_list[i]:
            return "IMPOSSIBLE"
    return count

def build_pancakes_list(cake_str):
    return [ch == '+' for ch in cake_str]

def main(cake_str, k):
    cake_list = build_pancakes_list(cake_str)
    return min_flip(cake_list, k)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    target = open('a-output.txt', 'w')
    for i in range(n):
        param = sys.stdin.readline().split(' ')
        target.write("case #{}: {}\n".format(i+1, main(param[0], int(param[1])))) 
                     