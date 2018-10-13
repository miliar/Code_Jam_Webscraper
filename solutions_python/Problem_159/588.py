__author__ = 'radykov'
import sys

def read_input():
    file = open('A-large.in', 'r')
    lines = file.read().split('\n')
    if lines[-1] == '':
        del lines[-1]
    return lines

def process_inputs(inputs):
    outfile = open('outfile.txt', 'w')
    for i in range(1, len(inputs), 2):
        if(input != ''):
            output = process_input(inputs[i+1])
            out_str =  'Case #' + str(i/2 + 1) + ": " + str(output[0]) + " " + str(output[1]) + '\n'
            outfile.write(out_str)

def process_input(input):
    string_arr = input.split(' ')
    arr = map(int, string_arr)
    out1 = method1(arr)
    out2 = method2(arr)
    out_arr = [out1, out2]
    return out_arr

def method1(arr):
    sum = 0
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            sum += arr[i] - arr[i+1]
    return sum

def method2(arr):
    max = max_diff(arr)
    return eaten_with_max(max, arr)



def eaten_with_max(max, arr):
    count = 0
    for i in range(0, len(arr)-1):
        if max > arr[i] :
            count += arr[i]
        else : count+= max

    return count

def max_diff(arr):
    max = 0
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            diff = arr[i] - arr[i+1]
            if diff > max:
                max = diff

    return max

inputs = read_input()
process_inputs(inputs)