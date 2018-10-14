import sys

sys.setrecursionlimit(1000000)

def makeNines(fromIndex, arr):
    for i in range(fromIndex, len(arr)):
        arr[i] = 9
    return arr

def resolveDisconnect(conflictingBeforeIndex, conflictingAfterIndex, arr):
    if conflictingBeforeIndex == 0:
        arr[conflictingBeforeIndex] -= 1
        return makeNines(1, arr)

    arr[conflictingBeforeIndex] -= 1

    if checkDisconnect(conflictingBeforeIndex - 1, conflictingBeforeIndex, arr):
        return resolveDisconnect(conflictingBeforeIndex - 1, conflictingBeforeIndex, arr)
    else:
        return makeNines(conflictingAfterIndex, arr)

def checkDisconnect(beforeIndex, afterIndex, arr):
    return arr[afterIndex] < arr[beforeIndex]

ret = []
with open('B-large.in', 'r') as file:
    t = int(file.readline())
    for _ in range(t):
        n = file.readline().strip()
        n_arr = map(int, list(n))
        for i in range(1, len(n_arr)):

            if checkDisconnect(i - 1, i, n_arr):
                n_arr = resolveDisconnect(i - 1, i, n_arr)
                break

        res = int(''.join([str(n) for n in n_arr]))
        # print res
        ret.append(res)

with open('b_large-out.txt', 'w') as outfile:
    for i in range(t):
        outfile.write("Case #%d: %s\n" % (i + 1, ret[i]))


# def isTidy(n):
#
#     n_arr = map(int, list(str(n)))
#     for i in range(1, len(n_arr)):
#         if n_arr[i] < n_arr[i-1]:
#             return False
#     return True
#
# def lastTidy(n):
#     while True:
#
#         if not isTidy(n):
#             n -=1
#         else:
#             return n

# import random
# n = random.randrange(10 ** 18)
