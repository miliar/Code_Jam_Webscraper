__author__ = 'User'
import math

def bathroom_split(k, n):
    p = 2 ** (math.floor(math.log(k, 2))) - 1
    section_size = (n - p)/(p + 1)
    if k - p - 1 < (n - p) % (p + 1):
        base_size = math.ceil(section_size)
    else:
        base_size = math.floor(section_size)
    edge = (base_size - 1) / 2
    min_s = math.floor(edge)
    max_s = math.ceil(edge)
    return min_s, max_s

with open("input.txt", "r") as file:
    with open("result.txt", "w") as write_file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            n, k = line.split(" ")
            min_s, max_s = bathroom_split(int(k), int(n))
            write_file.write("Case #{}: {} {}\n".format(i, max_s, min_s))
