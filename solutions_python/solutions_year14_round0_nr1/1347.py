#!/usr/bin/env python

def check(row1, row2):
    """
    Compute the intersection of row1 and row2, and
    1. if it contains a unique element: print it.
    2. if it contains more than one element: Bad magician!
    3. if it contains no element: Volunteer cheated!
    """
    intersection = list(set(row1) & set(row2))
    if len(intersection) == 1:
        return intersection[0]
    elif len(intersection) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

if __name__ == "__main__":
    import sys
    from string import strip, split
    line = sys.stdin.readline()
    num = int(line)
    for i in range(1, num+1):
        # read the first
        row1 = int(sys.stdin.readline()) - 1
        board1 = []
        for r in range(4):
            line = split(strip(sys.stdin.readline()))
            line = map(lambda x: int(x), line)
            board1.append(line)
        # read the second
        row2 = int(sys.stdin.readline()) - 1
        board2 = []
        for r in range(4):
            line = split(strip(sys.stdin.readline()))
            line = map(lambda x: int(x), line)
            board2.append(line)
        print "Case #%d:" %(i), check(board1[row1], board2[row2])

