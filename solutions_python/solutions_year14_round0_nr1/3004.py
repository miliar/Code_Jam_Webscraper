import sys

def solve(a, b):
    return [val for val in a if val in b]

numcases = int(sys.stdin.readline())
for casenum in range(1, numcases+1):
    first = int(sys.stdin.readline()) - 1
    first_array = []
    first_array.append(sys.stdin.readline().strip().split())
    first_array.append(sys.stdin.readline().strip().split())
    first_array.append(sys.stdin.readline().strip().split())
    first_array.append(sys.stdin.readline().strip().split())

    second = int(sys.stdin.readline()) - 1
    second_array = []
    second_array.append(sys.stdin.readline().strip().split())
    second_array.append(sys.stdin.readline().strip().split())
    second_array.append(sys.stdin.readline().strip().split())
    second_array.append(sys.stdin.readline().strip().split())

    intersection = solve(first_array[first], second_array[second])
    l = len(intersection)
    answer = "Volunteer cheated!"
    if l == 1 :
        answer = intersection[0]
    if l > 1 :
        answer = "Bad magician!"

    print("Case #{}: {}".format(casenum, answer))