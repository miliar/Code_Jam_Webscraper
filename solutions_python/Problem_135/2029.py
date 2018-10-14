import sys

def read_one_int():
    return int(sys.stdin.readline().strip())

def read_line_int():
    return [int(i) for i in sys.stdin.readline().strip().split()]

N = int(sys.stdin.readline().strip())

for n in range(N):
    c1 = read_line_int()[0]
    for i in range(4):
        if i != c1-1:
            sys.stdin.readline()
        else:
            r1 = set(read_line_int())

    c2 = read_line_int()[0]
    for i in range(4):
        if i != c2-1:
            sys.stdin.readline()
        else:
            r2 = set(read_line_int())

    i = list(r1.intersection(r2))


    if len(i) == 1:
        result = i[0]
    elif len(i) > 1:
        result = "Bad magician!"
    else:
        result = "Volunteer cheated!"

    print("Case #{}: {}".format(n+1, result))

