import math as m

def validate(ranges, x):
    copy = list([list(x) for x in ranges])
    for row in copy:
        found = False
        for j in range(len(row)):
            if row[j][0] <= x <= row[j][1]:
                found = True
                break

        if found:
            row.remove(row[j])
        else:
            return False, ranges

    return True, copy


def solve(n, p, ratatui, pieces):
    ranges = []
    for i in range(len(ratatui)):
        tmp = []
        for value in pieces[i]:
            max = value/(0.9*ratatui[i])
            min = value/(1.1*ratatui[i])
            tmp.append((m.ceil(min), m.floor(max)))

        tmp.sort()
        ranges.append(tmp)

    checked = set()
    tmp = [item for sublist in ranges for item in sublist]
    flatten = [x[0] for x in tmp] + [x[1] for x in tmp]
    flatten.sort()
    kits_count = 0

    for r in flatten:
        if r in checked:
            continue

        checked.add(r)
        result = True
        while result:
            result, ranges = validate(ranges, r)
            if result:
                kits_count += 1

    return str(kits_count)



def main():
    t = int(input())
    for i in range(1, t + 1):
        n, p = [int(s) for s in input().split(" ")]
        ratatui = [int(s) for s in input().split(" ")]
        pieces = []
        for j in range(n):
            pieces.append([int(s) for s in input().split(" ")])

        print(f"Case #{i}: {solve(n, p, ratatui, pieces)}")


if __name__ == "__main__": main()