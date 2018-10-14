
def solve(array):
    for i in range(len(array)):
        if i != (len(array) - 1):
            if array[-i - 1] < array[-i - 2] or array[-i - 1] == 0:
                if (-i - 1) != (-len(array) + 1):    
                    array[-i - 1] = 9
                    if array[-i - 2] == 0:
                        array[-i - 2] = 9
                    else:
                        array[-i - 2] -= 1
    return array
def solve2(array):
    for i in range(len(array)):
        if i != (len(array) - 1):
            if array[-i - 1] < array[-i - 2] or array[-i - 1] == 0:
                if (-i - 1) != (-len(array) + 1):    
                    array[-i - 1] = 9
    return array

def change(array):
    array.pop(0)
    for i in range(len(array)):
        array[i] = str(array[i])
    res = int(''.join(array))
    return res

tests = int(input())

for test in range(tests):
    array = [0]
    number = input().split()
    for i in range(len(number[0])):
        array.append(int(number[0][i]))
    array = solve(array)
    for i in range(18):
        array =solve2(array)
    res = change(array)
    print("Case #%d:" % (test + 1), res)