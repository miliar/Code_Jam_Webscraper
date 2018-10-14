def solve(hint1, cards1, hint2, cards2):
    opt1 = set(cards1[hint1 - 1])
    opt2 = set(cards2[hint2 - 1])
    possible = opt1 & opt2
    if len(possible) == 0:
        return 'Volunteer cheated!'
    if len(possible) > 1:
        return 'Bad magician!'
    return list(possible)[0]


def test_example1():
    assert solve(2, [[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]],
                 3, [[1, 2, 5, 4],
                     [3, 11, 6, 15],
                     [9, 10, 7, 12],
                     [13, 14, 8, 16]]) == 7


def test_example2():
    assert solve(2,
                 [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]],
                 2,
                 [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]) == 'Bad magician!'


def test_example3():
    assert solve(2,
                 [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]],
                 3,
                 [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]) == 'Volunteer cheated!'

if __name__ == "__main__":

    import sys
    data = open(sys.argv[1] + '.in').readlines()
    outfile = open(sys.argv[1] + '.out', 'w')
    t = int(data[0])
    data = data[1:]
    for i in range(t):
        block = data[:10]
        hint1 = int(block[0].strip())
        hint2 = int(block[5].strip())
        cards1 = [map(int, row.strip().split()) for row in block[1:5]]
        cards2 = [map(int, row.strip().split()) for row in block[6:]]

        answer = solve(hint1, cards1, hint2, cards2)
        outfile.write("Case #%i: %s\n" % (i + 1, answer))
        data = data[10:]
