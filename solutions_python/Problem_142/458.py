from sys import stdin
import math

file = stdin

def read_line():
    return file.readline().strip()

def read_int():
    return int(read_line())

def word_to_list(word):
    lst =  list(word)
    prev = 0
    letter = []
    count = []
    for w in lst:
        if w != prev:
            letter.append(w)
            count.append(1)
            prev = w
        else:
            count[-1] = count[-1] + 1
    return [letter, count]
def find_deviation(counts):
    counts.sort()
    mid = len(counts)//2
    mid_element = counts[mid]
    diff = 0
    for count in counts:
        diff = diff + abs(mid_element - count)
    return diff
def process(length, lst):
    table_head = None
    doable = True
    count_arrays = []
    for word in lst:
        [letter, count] = word_to_list(word)
        if table_head == None:
            table_head = letter
            for x in range(len(table_head)):
                count_arrays.append([])

        elif table_head != letter:
            doable = False
            break
        for x in range(len(count)):
            count_arrays[x].append(count[x])
    if doable:
        diff = 0
        for counts in count_arrays:
            diff = diff + find_deviation(counts)
        return str(diff)
    else:
        return "Fegla Won"

cases = read_int()
for case_no in range(1, cases+1):
    n = read_int()
    lst = []
    for ns in range(n):
        line = read_line()
        lst.append(line)
    out = process(n, lst)
    print("Case #{0}: {1}".format(case_no, out))
