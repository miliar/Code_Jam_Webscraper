def solve(row1, answer1, row2, answer2):
    result = set(row2[answer2]) & set(row1[answer1])

    if len(result) == 0:
        return "Volunteer cheated!"

    if len(result) > 1:
        return "Bad magician!"

    return list(result)[0]

for case in range(int(raw_input())):
    answer1 = int(raw_input())
    row1 = [map(int, raw_input().split()),
            map(int, raw_input().split()),
            map(int, raw_input().split()),
            map(int, raw_input().split())]

    answer2 = int(raw_input())

    row2 = [map(int, raw_input().split()),
            map(int, raw_input().split()),
            map(int, raw_input().split()),
            map(int, raw_input().split())]

    print "Case #%d: %s" % (case+1, solve(row1, answer1-1, row2, answer2-1))