import copy

def invert_values(arr, i, k):
    for p in range(i, i+k):
        if arr[p] == "+":
            arr[p] = "-"
        else:
            arr[p] = "+"
    return arr

def reverse(arr):
    arr.reverse()
    return arr

def allPos(arr):
    for i in range(len(arr)):
        if(arr[i] == "-"):
            return 0
    return 1

file = open("A-small-attempt2.in", "r")
out = open("out.txt", "w")
i = 0
line_count = 0
for line in file:
    arr=line.split(" ")
    tmp = arr[0]
    k = int(arr[1])
    row = list(tmp)
    flip_count = 0
    loop = 0
    while allPos(row) != 1 and flip_count != 'IMPOSSIBLE':
        if(row[i] == '-'):
            if i + k -1 < len(row):
                row = invert_values(row, i, k)
                flip_count = flip_count + 1
                i = 0
            else:
                new_row = reverse(row)
                i = 0
        else:
            i = i+1
        loop = loop + 1
        if(loop > 100):
            flip_count = 'IMPOSSIBLE'
            i = 0
            break
    line_count = line_count + 1
    out.write("Case #"+str(line_count)+ ": "+ str(flip_count) + "\n")