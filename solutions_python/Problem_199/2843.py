import os

input_file = open("input_large.in", "r")
output_file = open("output_large.out", "w")

cases = int(input_file.readline())

for i in range(cases):
    params = input_file.readline().split(" ")
    arr = params[0]
    arr = [False if x == "-" else True for x in arr]
    flipper_size = int(params[1])

    finished = False
    num_flips = 0

    while not finished:
        if 0 in arr:
            index_first = arr.index(0)
            if index_first + flipper_size <= len(arr):
                for j in range(flipper_size):
                    arr[index_first + j] = not arr[index_first + j]
                num_flips += 1
            else:
                num_flips = -1
                finished = True
        else:
            finished = True

    if num_flips >= 0:
        output_file.write("Case #" + str(i + 1) + ": " + str(num_flips) + "\n")

    else:
        output_file.write("Case #" + str(i + 1) + ": IMPOSSIBLE" + "\n")






