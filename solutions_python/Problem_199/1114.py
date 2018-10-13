# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def swap_face(x):
    if x == '+':
        return '-'
    else:
        return '+'

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    inp = input().split(' ')
    pancakes = inp[0]
    k = int(inp[1])
    swaps = 0
    actual = '+'
    actual_k = []
    for j in range(len(pancakes)):
        p = pancakes[j]
        if len(actual_k) > 0:
            if actual_k[0] <= j:
                actual = swap_face(actual)
                actual_k.pop(0)
        else:
            actual = '+'
        if p != actual:
            if len(pancakes) - j < k:
                swaps = -1
                break
            actual = swap_face(actual)
            actual_k.append(k+j)
            swaps += 1
    if swaps < 0:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: {}".format(i, swaps))
