

def solution(n, k):
    if n == k:
        return (0,0)
    l = [(0,n)] #(start index, size)
    left, right = 0, 0
    for i in range(k):
        # print(l)
        first, size = l.pop(0)
        if size % 2 != 0:
            occupiedStall = size // 2 + first
            # print("Occupied Stall : {}".format(occupiedStall))
            left = occupiedStall - first
            right = size - left - 1
            l.append((first, left))
            l.append((occupiedStall + 1, right))
        else:
            occupiedStall = size // 2 - 1 + first
            # print("Occupied Stall : {}".format(occupiedStall))
            left = occupiedStall - first
            right = size - left - 1
            l.append((first, left))
            l.append((occupiedStall + 1, right))
        l.sort(key = lambda t: (-t[1],t[0]))
    if left == -1 and right == -1:
        left, right = 0, 0
    return (left, right)


file = open('input.txt')
tests = int(file.readline())
cases = []
for t in range(tests):
    cases.append(file.readline().strip().split(' '))

test = 0
for n, k in cases:
    test += 1
    l, r = solution(int(n),int(k))
    print("Case #{}: {} {}".format(test, max([l,r]),min([l,r])))
