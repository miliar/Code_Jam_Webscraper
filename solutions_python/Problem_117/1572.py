import sys


def possible(field):
    cols = set([])
    for row in range(len(field)):
        m = max(field[row])
        for col in range(len(field[0])):
            if field[row][col] != m:
                cols.add(col)

    for col in cols:
        m = field[0][col]
        for row in range(1, len(field)):
            if field[row][col] != m:
                return False
    return True


if __name__ == "__main__":
    num_testcases = int(sys.stdin.readline())
    for i in range(1, num_testcases+1):
        tokens = sys.stdin.readline().split(" ")
        n = int(tokens[0])

        field = []

        for j in range(n):
            field.append([int(x.strip()) for x in sys.stdin.readline().split(" ")])
        #print field
        r = "YES" if possible(field) else "NO"
        print("Case #{n}: {r}".format(n=i, r=r))