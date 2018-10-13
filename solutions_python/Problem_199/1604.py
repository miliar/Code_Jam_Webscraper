
def flip(stack, index, k):
    assert index >= 0
    assert index + k <= len(stack)
    for i in range(index,k + index):
        if i >= len(stack):
            break
        if stack[i] == "+":
            stack[i] = "-"
        elif stack[i] == "-":
            stack[i] = "+"
    return stack

def isSolution(s):
    for i in s:
        if i != "+":
            return False
    return True

def solve(cakes, k):

    for i in range(0, len(cakes)):
        temp = list(cakes)
        count = 0
        for j in range(i, len(temp)):
            if isSolution(temp):
                return count
            elif temp[j] == "-" and j + k <= len(temp):
                temp = flip(temp, j, k)
                count += 1

    return "Impossible"


# i/o handling
N = int(input().strip())
for i in range(0, N):
    case = input().strip().split(" ")
    r = solve(case[0], int(case[1]))
    print("Case #{}: {}".format(i + 1, r))
