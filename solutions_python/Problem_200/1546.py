from sys import stdin

cases = int(stdin.readline())

def doit(arr, index):
    if index >= 0:
        arr[index] = arr[index]-1
        arr = arr[:index+1] + [9] * (len(arr) - index - 1)
        if arr[index - 1] > arr[index]:
            return doit(arr, index - 1)
        else:
            return arr
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            return doit(arr, j)
    return arr

for i in range(cases):
    n = stdin.readline()
    digs = []
    for s in n:
        if s != '\n':
            digs.append(int(s))
    strin = ""
    ans = doit(digs, -1)
    for cha in ans:
        if cha != 0:
            strin += str(cha)
    print "Case #"+str(i+1)+": "+strin
