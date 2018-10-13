# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math

powers_of_2 = dict()
n = 1
for i in range(70):
    powers_of_2[i] = n
    n *= 2

def look_for_m(k):
    for i in range(len(powers_of_2)-1):
        if k < powers_of_2[i+1] and k >= powers_of_2[i]:
            return i, powers_of_2[i]
    return -1, -1

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    inp = input().split(' ')
    n = int(inp[0])
    k = int(inp[1])
    m, two_at_m = look_for_m(k)
    #print("m: {}".format(m))
    s = (n - (two_at_m - 1)) / two_at_m
    #print("s: {}".format(s))
    s1 = (s - math.floor(s)) * two_at_m
    #print("s1: {}".format(s1))
    s = math.floor(s)
    if k - two_at_m < s1:
        y, z = math.ceil((s) / 2), math.floor((s) / 2)
    else:
        y, z = math.ceil((s - 1) / 2), math.floor((s - 1) / 2)
    print("Case #{}: {} {}".format(i, y, z))
