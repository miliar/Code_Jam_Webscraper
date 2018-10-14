import sys

def test(f):
    first_guess = int(f.readline().strip()) - 1
    rows = [{},{},{},{}]
    for i in range(4):
        rows[i] = set(f.readline().split())
    first_row = rows[first_guess]
    second_guess = int(f.readline().strip()) - 1
    for i in range(4):
        rows[i] = set(f.readline().split())
    second_row = rows[second_guess]
    intersect = first_row.intersection(second_row)
    if len(intersect) == 0:
        return "Volunteer cheated!"
    elif len(intersect) == 1:
        return intersect.pop()
    else:
        return "Bad magician!"

def main(argv):
    if len(argv) < 2:
        return
    filename = argv[1]
    with open(filename) as f:
        num_tests = int(f.readline())
        for i in range(num_tests):
            res = test(f)
            print( "Case #", i+1, ": ", res, sep='')

if __name__ == "__main__":
    main(sys.argv)