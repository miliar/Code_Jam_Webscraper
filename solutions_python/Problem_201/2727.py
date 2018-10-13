#!/usr/bin/env python3

def read_ints():
    return [int(i) for i in input().split()]

def read_int():
    return read_ints()[0]

def calculate_left_distance(arr):
    length = len(arr)
    result = [None] * length
    for i in range(length):
        if arr[i]:
            result[i] = -1
        else:
            result[i] = result[i-1] + 1 # guarded, so it's safe
    return result

def calculate_right_distance(arr):
    length = len(arr)
    result = [None] * length
    for i in range(length-1, -1, -1):
        if arr[i]:
            result[i] = -1
        else:
            result[i] = result[i+1] + 1 # guarded, so it's safe
    return result
    

def add_person(arr):
    left = calculate_left_distance(arr)
    right = calculate_right_distance(arr)
    best_idx = 0
    min_max = -1
    max_max = -1
    for i in range(len(arr)):
        min_cur = min(left[i], right[i])
        max_cur = max(left[i], right[i])
        if min_cur > min_max:
            min_max = min_cur
            max_max = max_cur
            best_idx = i
        elif min_cur == min_max and max_cur > max_max:
            min_max = min_cur
            max_max = max_cur
            best_idx = i
    arr[best_idx] = 1
    return max_max, min_max

def solve(n, k):
    arr = [1] + [0] * n + [1]
    for _ in range(k):
        result = add_person(arr)
        #print(arr)
    return result 

def main():
    ncases = read_int()
    for i in range(1, ncases+1):
        n, k = read_ints()
        s1, s2 = solve(n, k)
        print('Case #%d: %d %d' % (i, s1, s2))


if __name__ == '__main__':
    main()
