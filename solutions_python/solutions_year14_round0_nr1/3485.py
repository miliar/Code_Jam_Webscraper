import sys

def read_cases(f):
    """Parse the test cases from f."""
    no = int(f.readline().strip())
    for i in range(no):
        rowA = int(f.readline().strip())
        gridA = [list(map(int, f.readline().strip().split())) for j in range(4)]
        rowB = int(f.readline().strip())
        gridB = [list(map(int, f.readline().strip().split())) for j in range(4)]
        yield rowA, gridA, rowB, gridB

def main():
    for i, case in enumerate(read_cases(sys.stdin), 1):
        sys.stdout.write("Case #" + str(i) + ": ")
        rowA, gridA, rowB, gridB = case
        values = set(gridA[rowA - 1]) & set(gridB[rowB - 1])
        if len(values) == 0:
            sys.stdout.write("Volunteer cheated!\n")
        elif len(values) == 1:
            for value in values: # and there is only one
                sys.stdout.write(str(value) + "\n")
        else:
            sys.stdout.write("Bad magician!\n")

main()
