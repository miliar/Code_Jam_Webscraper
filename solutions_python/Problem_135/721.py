import sys

tc = int(sys.stdin.readline().strip())

for i in range(tc):
    idx = int(sys.stdin.readline().strip())
    matrix = [[int(v.strip()) for v in sys.stdin.readline().strip().split()] for _ in range(4)]
    candidates = set(matrix[idx-1])

    idx = int(sys.stdin.readline().strip())
    matrix = [[int(v.strip()) for v in sys.stdin.readline().strip().split()] for _ in range(4)]
    candidates = candidates.intersection(matrix[idx-1])

    if len(candidates) == 0:
        print("Case #%d: Volunteer cheated!" % (i+1))
    elif len(candidates) > 1:
        print("Case #%d: Bad magician!" % (i+1))
    else:
        print("Case #%d: %d" % (i+1, candidates.pop()))
