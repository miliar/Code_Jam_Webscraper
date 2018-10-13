def isGoal(n):
    for i in range(0, len(n)-1):
        if n[i] < n[i+1]:
            return False
    return True

def solution(n):
    if len(n) == 1:
        return int(''.join(map(str, n)))
    for i in range(0, len(n)-1):
        if n[i] > n[i+1]:
            n[i] -= 1
            for j in range(i+1, len(n)):
                n[j] = 9
            if isGoal(n):
                return int(''.join(map(str, n)))
            else:
                return solution(n)
    return int(''.join(map(str, n)))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = str(input()) # s = String, n = Number of flip per flipper
    arr =[]
    for j in range (0, len(n)):
        arr.append(int(n[j]))
    print("Case #{}: {}".format(i, solution(arr)))
