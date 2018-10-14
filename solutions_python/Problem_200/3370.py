lines = []
with open("B-large.in", 'r') as reader:
   lines = reader.readlines()
t = int(lines[0])
lines = lines[1:]
out = open("B-large.out", 'w')

def solution(num):
    arr = numToArr(num)
    l = len(arr)
    for _ in range(len(arr)):
        i = 0
        while i < len(arr) - 1:
            if arr[i] > arr[i + 1]:
                arr[i] -= 1
                i += 1
                while i < len(arr):
                    arr[i] = 9
                    i += 1
            i += 1
    return arrToNum(arr)

def numToArr(num):
    arr = []
    while num > 0:
        arr.insert(0, num % 10)
        num //= 10
    return arr

def arrToNum(arr):
    num = 0
    while arr != []:
        num *= 10
        num += arr.pop(0)
    return num

for i in range(t):
    out.write("Case #" + str(i + 1) + ': ' + str(solution(int(lines[i]))) + "\n")

