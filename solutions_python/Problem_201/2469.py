x = int(input())


def split(total):
    if total % 2 == 0:
        left = total / 2.0
        right = total / 2.0 - 1
    else:
        left, right = total / 2.0, total / 2.0
        left = int(left)
        right = int(right)

    return int(left), int(right)


for k in range(1, x+1):
    seats, people = [int(y) for y in input().split(" ")]
    l, r = 0, 0

    been_there = []
    for x in range(people):
        l, r = split(seats)
        been_there.append(r)
        been_there.append(l)
        seats = max(been_there)
        been_there.remove(max(been_there))

    print("Case #{}: {} {}".format(k, l, r))