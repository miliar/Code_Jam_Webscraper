import sys

def read_cases(f):
    """Parse the test cases from f."""
    no = int(f.readline().strip())
    for i in range(no):
        yield tuple(map(float, f.readline().strip().split()))

def main():
    for i, case in enumerate(read_cases(sys.stdin), 1):
        sys.stdout.write("Case #" + str(i) + ": ")
        C, F, X = case
        mintime = min((sum((C / (2 + F * a)) for a in range(f)) + X / (2 + F * f)) for f in range(0, int(1 + X / C)))
        sys.stdout.write(str(mintime) + '\n')

main()
