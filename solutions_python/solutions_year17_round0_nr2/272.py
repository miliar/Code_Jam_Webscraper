import sys

def int_to_array(i):
    to_return = []
    while i > 0:
        to_return.insert(0, i % 10)
        i = int(i/10)
    return to_return

def array_to_int(arr):
    to_return = 0
    curr = 1
    i = len(arr)-1
    while i >= 0:
        to_return += arr[i]*curr
        curr *=10
        i -= 1
    return to_return

#returns string    
def solution(line):
    to_return = int_to_array(int(line))
    i = len(to_return)-1
    while i > 0:
        if to_return[i] < to_return[i-1]:
            for k in range(i,len(to_return)):
                to_return[k] = 9
            to_return[i-1] -= 1
        i-=1
    return str(array_to_int(to_return))
            
in_file = sys.argv[1]
in_stream = open(in_file)
lines = in_stream.readlines()


for i in range(1,len(lines)):
    print 'Case #%d: '%i +solution(lines[i])
