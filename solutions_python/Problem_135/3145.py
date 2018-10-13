import sys

def get_lines(f, n):
    total = []
    for i in range(n):
        total.append(f.readline())
    return total

def solve(lines):
    answer_1 = int(lines[0])
    #print answer_1
    row_1 = lines[answer_1]
    #print row_1
    answer_2 = int(lines[5])
    #print answer_2
    row_2 = lines[answer_2 + 5]
    #print row_2
    count = 0
    #print row_1.split()
    #print row_2.split()
    for c in row_1.split():
        if c in row_2.split():
            card = c
            count += 1
    if count == 1:
        return card
    elif count == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


def main():
    file_name = sys.argv[1]
    with open(file_name) as f:
        test_cases = int(f.readline())
        for i in range(test_cases):
            lines = get_lines(f, 10)
            result = solve(lines)
            out = "Case #%d: %s" % (i + 1, result)
            print out.strip()

if __name__ == '__main__':
    main()
